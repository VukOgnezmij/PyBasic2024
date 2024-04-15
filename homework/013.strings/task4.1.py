from string import Template
from textwrap import dedent


bd_id = 84
intf_start = "10GE1/0/1"
intf_end = "10GE1/0/48"
rid = "192.168.43.34"
bgp_as = 64512


config_template = Template("#\n"
    "bridge-domain $t_bd_id\n"
    " vlan $t_bd_id access-port interface $t_intf_start to $t_intf_end\n"
    " vxlan vni $t_vxlan_vni\n"
    " #\n"
    " evpn\n"
    "  route-distinguisher $t_rid:$t_rd_rt\n"
    "  vpn-target $t_bgp_as:$t_rd_rt export-extcommunity\n"
    "  vpn-target $t_bgp_as:$t_rd_rt import-extcommunity\n"
    " arp broadcast-suppress enable\n"
    "#\n")

bd_id = str(bd_id)
if len(bd_id) < 4:
    zero_req = 4 - len(bd_id)
    vxlan_vni = "1" + bd_id.rjust(zero_req + len(bd_id), "0")
    rd_rt = vxlan_vni
else:
    vxlan_vni = "1" + bd_id
    rd_rt = vxlan_vni


config = config_template.safe_substitute(t_bd_id=bd_id, t_intf_start=intf_start, t_intf_end=intf_end, t_rid=rid, t_bgp_as=bgp_as, t_vxlan_vni=vxlan_vni, t_rd_rt=rd_rt)

print(config)