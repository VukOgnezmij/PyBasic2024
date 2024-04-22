from collections import namedtuple

output = """
Interface             IP-Address      OK?    Method Status      Protocol
GigabitEthernet0/2    192.168.190.235 YES    unset  up          up
GigabitEthernet0/4    192.168.191.2   YES    unset  up          down
TenGigabitEthernet2/1 unassigned      YES    unset  up          up
Te36/45               unassigned      YES    unset  down        down
""".strip()

output = output.split("\n")
del output[0]
InterfaceStatus = namedtuple("intf_brief", ["name", "ip", "status"])

intf_brief = []
for line in output:
    intf = line.split()
    intf_brief.append(InterfaceStatus(intf[0], intf[1], intf[4]))

print(isinstance(intf_brief, list))
print(len(intf_brief))
print(intf_brief[0].name)
print(intf_brief[0].ip)
print(intf_brief[0].status)