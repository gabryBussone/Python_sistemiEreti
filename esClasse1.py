import ipaddress

def controlla_privato_o_loopback(indirizzo_ip, subnet_mask):
    try:
        rete = ipaddress.IPv4Network(f"{indirizzo_ip}/{subnet_mask}")
    except ValueError:
        print("Errore: Indirizzo IP o subnet mask non validi.")
        return

    if rete.is_private:
        print(f"L'indirizzo IP {indirizzo_ip} è privato.")
    elif rete.is_loopback:
        print(f"L'indirizzo IP {indirizzo_ip} è loopback.")
    else:
        print(f"L'indirizzo IP {indirizzo_ip} non è né privato né loopback.")

def stampa_indirizzi_utilizzabili(indirizzo_ip, subnet_mask):
    try:
        rete = ipaddress.IPv4Network(f"{indirizzo_ip}/{subnet_mask}")
    except ValueError:
        print("Errore: Indirizzo IP o subnet mask non validi.")
        return

    if rete.is_private or rete.is_loopback:
        print("L'indirizzo IP è privato o loopback, non ci sono IP utilizzabili.")
    else:
        print("Indirizzo di rete valido. Gli indirizzi IP utilizzabili sono:")
        for host in rete.hosts():
            print(host)

def main():
    indirizzo_ip = input("Inserisci l'indirizzo IP: ")
    subnet_mask = input("Inserisci la subnet mask: ")

    controlla_privato_o_loopback(indirizzo_ip, subnet_mask)
    stampa_indirizzi_utilizzabili(indirizzo_ip, subnet_mask)

if __name__ == "__main__":
    main()

