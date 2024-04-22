SCRAPLI_TEMPLATE = {
    "auth_username": "cisco",
    "auth_password": "password",
    "transport": "system",
    "auth_strict_key": False,
    "port": 22,
}

device1 = SCRAPLI_TEMPLATE | {"hostname": "sw1.abcd.net"}
device2 = SCRAPLI_TEMPLATE | {"hostname": "sw1.abcd.net", "transport": "telnet", "port": 23}
print(device1)
print(device2)
print(SCRAPLI_TEMPLATE)