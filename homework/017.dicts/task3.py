device1 = {
    "hostname": "r1.abcd.net",
    "ip": "192.168.1.1",
    "username": "cisco",
    "password": "secret",
    "platform": "cisco_ios",
    "enable": "True"
}

device2 = {
    "hostname": "sw1.abcd.net",
    "ip": "192.168.1.2",
    "username": "admin",
    "password": "secret",
    "platform": "huawei_vrp",
    "enable": "False"
}

devices_list = [device1, device2]

device3 = {
    "hostname": "wlc.abcd.net",
    "ip": "192.168.1.3",
    "username": "wlc_admin",
    "password": "password",
    "enable": "False"
}

devices_list.append(device3)
device_dict = {}

for device in devices_list:
    device_dict[device["hostname"]] = {}
    device_dict[device["hostname"]].update(device)
    
print(device_dict)    
