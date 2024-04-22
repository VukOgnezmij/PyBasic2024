output = "switchport trunk allowed vlan 2,101,104"

trunk_allowed = output.split(" ")
vlan = trunk_allowed[4].split(",")

print(vlan)