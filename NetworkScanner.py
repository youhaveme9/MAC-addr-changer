#!/usr/bin/env python

import scapy.all as scapy
import optparse


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


def get_input():
    parser = optparse.OptionParser()
    parser.add_option("-t", "--target", dest="target", help="Specify IP or IP range")
    (opt, args) = parser.parse_args()
    if not opt.target:
        parser.error("[-] Please specify an target, use --help for more info")
    return opt


if __name__ == '__main__':
    ip_target = get_input()
    datas = scan(ip_target.target)
    print_result(datas)
