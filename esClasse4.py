import ipaddress

def main():
    ip_addresses = ["192.168.222.0/27", "192.168.100.0/24", "192.168.200.0/28", "192.168.50.0/22"]

    with open("mask.txt", "w") as file:
        for ip_address in ip_addresses:
            network = ipaddress.IPv4Network(ip_address, strict=False)
            subnet_mask = network.netmask
            file.write(f"{ip_address}: {subnet_mask}\n")

if __name__ == "__main__":
    main()