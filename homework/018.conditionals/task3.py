access = """
interface {if_name}
   switchport mode access
   switchport access vlan {vlan}
!
""".strip()

trunk = """
interface {if_name}
   switchport mode trunk
   switchport trunk allowed vlan {vlan}
!
""".strip()

intf1 = {
    "if_name": "gi0/1",
    "vlan": 102,
    "mode": "access",
}

intf2 = {
    "if_name": "gi0/2",
    "vlan": 103,
    "mode": "trunk",
}

print("с использованием условий (т.е. с if):\n")

if intf1.get("mode") == "access":
    intf1_config = access.format(if_name = intf1.get("if_name"), vlan = intf1.get("vlan"))
    print(intf1_config)

if intf2.get("mode") == "trunk":
    intf2_config = trunk.format(if_name = intf2.get("if_name"), vlan = intf2.get("vlan"))
    print(intf2_config)
    
print("\nбез использования условий (без if):\n")
    
match intf1.get("mode"):
    case "access":
        intf1_config = access.format(if_name = intf1.get("if_name"), vlan = intf1.get("vlan"))
        print(intf1_config)

match intf2.get("mode"):
    case "trunk":
        intf2_config = trunk.format(if_name = intf2.get("if_name"), vlan = intf2.get("vlan"))
        print(intf2_config)