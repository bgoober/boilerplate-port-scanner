import socket
import common_ports

def get_open_ports(target, port_range, verbose = False):
    open_ports = []

    # Check if the target is a valid IP address
    try:
        socket.inet_aton(target)
        is_ip = True
    except socket.error:
        is_ip = False

    # Resolve the hostname
    try:
        ip_address = socket.gethostbyname(target)
        if is_ip:
            hostname = socket.gethostbyaddr(ip_address)[0]
        else:
            hostname = target
    except:
        if is_ip:
            return "Error: Invalid IP address"
        else:
            return "Error: Invalid hostname"
    
    # Scan the ports
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    # Generate the verbose output
    if verbose:
        output = f"Open ports for {hostname} ({ip_address})\nPORT     SERVICE"
        for port in open_ports:
            output += f"\n{port}       {common_ports.ports_and_services[port]}"
        return output.strip()
    else:
        return open_ports