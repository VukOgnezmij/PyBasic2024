intf_list = ["gi0/0", "gi0/1", "gi0/22", "gi0/23", "gi0/3", "gi0/4"]

intf_list.append("gi0/2")
intf_list.sort()
delete_intf = {"gi0/22", "gi0/23"}

intf_list = [inf for inf in intf_list if inf not in delete_intf]

print(intf_list)