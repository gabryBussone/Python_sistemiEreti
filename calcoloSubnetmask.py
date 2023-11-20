def calculate_subnet_mask(cidr):
 
    subnet_mask = "1" * cidr + "0" * (32 - cidr)
    
    octets = [subnet_mask[i:i + 8] for i in range(0, 32, 8)]
    
    decimal_octets = [str(int(octet, 2)) for octet in octets]
    
    subnet_mask_str = ".".join(decimal_octets)
    
    return subnet_mask_str

cidr = 29 
subnet_mask = calculate_subnet_mask(cidr)
print("Subnet Mask:", subnet_mask)

