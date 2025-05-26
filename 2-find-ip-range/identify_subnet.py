import ipaddress

def get_subnet(ip, netmask):
    # Combine IP and netmask into a network address
    network = ipaddress.IPv4Network(f"{ip}/{netmask}", strict=False)
    return network

# Example values — replace with your own if needed
ip_address = "192.168.1.5"
subnet_mask = "255.255.255.0"

subnet = get_subnet(ip_address, subnet_mask)
print(f"Network Address: {subnet.network_address}")
print(f"Subnet: {subnet.with_prefixlen}")
print(f"Usable Hosts: {subnet.num_addresses - 2}")
print(f"Host Range: {list(subnet.hosts())[0]} - {list(subnet.hosts())[-1]}")
