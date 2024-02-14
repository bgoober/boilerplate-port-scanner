import socket

import common_ports

def get_open_ports(target, port_range, verbose = False):
    open_ports = []

    try:
        ip_address = socket.gethostbyname(target)
    except:
        return("Error: Invalid hostname")
    
    if ip_address == target:
        return("Error: Invalid IP address")
    
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    if verbose:
        output = f"Open ports for {target} ({ip_address})\nPORT     SERVICE\n"
        for port in open_ports:
            output += f"{port}       {common_ports.ports_and_services[port]}\n"
        return(output)
    else:
        return(open_ports)
    
print(get_open_ports("localhost", [79, 82], True))