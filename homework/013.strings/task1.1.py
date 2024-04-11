config = (
    "#\n"
    "bridge-domain 555\n"
    " vlan 555 access-port interface 10GE1/0/1 to 10GE1/0/48\n"
    " vxlan vni 10555\n"
    " #\n"
    " evpn\n"
    "  route-distinguisher 192.168.43.34:10555\n"
    "  vpn-target 64512:10555 export-extcommunity\n"
    "  vpn-target 64512:10555 import-extcommunity\n"
    " arp broadcast-suppress enable\n"
    "#\n"
)
print(config)