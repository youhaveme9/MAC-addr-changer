#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    arp_req = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broadcast = broadcast / arp_req
    answered = scapy.srp(arp_req_broadcast, timeout=1, verbose=False)[0]
    mac_list = []
    for element in answered:
        mac_dict = {
            "ip": element[1].psrc,
            "mac": element[1].hwsrc
        }
        mac_list.append(mac_dict)
    return mac_list


def print_result(result):
    print("-" * 50)
    print("IP\t\tMac Address")
    print("-" * 50)
    for data in result:
        print(data["ip"] + "\t" + data["mac"])


datas = scan("192.168.66.1/24")
print_result(datas)


