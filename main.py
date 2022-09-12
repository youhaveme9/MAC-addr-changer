#!/usr/bin/env python3

import subprocess
import optparse
import re


# subprocess.call('ifconfig', shell=True)
def get_input():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="iface", help="Interface name to change its MAC address")
    parser.add_option("-m", "--mac", dest="mac_addr", help="New MAC address")
    (opt, args) = parser.parse_args()
    if not opt.iface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not opt.mac_addr:
        parser.error("[-] Please specify a mac address, use --help for more info")
    return opt


def change_mac(iface, mac):
    print(f"[+] Changing MAC Address of {iface} to {mac}")
    subprocess.call(f"ifconfig {iface} down", shell=True)
    subprocess.call(f"ifconfig {iface} hw ether {mac}", shell=True)
    subprocess.call(f"ifconfig {iface} up", shell=True)


def get_mac(interface):
    output = subprocess.check_output(['ifconfig', interface])
    mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(output))
    if mac_address:
        return mac_address.group(0)
    else:
        print("[-] Could not read the mac address")


opt = get_input()

current_mac = get_mac(opt.iface)
print(f"Current MAC = {current_mac}")
change_mac(opt.iface, opt.mac_addr)
final_mac = get_mac(opt.iface)
if final_mac == opt.mac_addr:
    print(f"[+] Mac address changed successfully to {opt.mac_addr}")
else:
    print("[-] Mac address did not changed")
