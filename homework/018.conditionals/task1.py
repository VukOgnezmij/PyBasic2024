mac_list = ["50-46-5D-6E-8C-20", "50-46-5d-6e-8c-20", "50:46:5d:6e:8c:20", "50465d6e8c20", "50465d:6e8c20", "5046:5d6e:8c20"]

for mac in mac_list:
    if mac.find("-") != -1 and mac.count("-") == 5:
        mac_str = mac.replace("-", "")
        if mac_str.isupper() == True:
            mac_notation = "IEEE EUI-48"
            print(f"нотация {mac}: {mac_notation}")
        else:
            mac_notation = "IEEE EUI-48 lowercase"
            print(f"нотация {mac}: {mac_notation}")
    elif mac.find("-") == -1 and mac.find(":") != -1:
        if mac.count(":") == 5:
            mac_str = mac.replace(":", "")
            mac_notation = "UNIX"
            print(f"нотация {mac}: {mac_notation}")
        elif mac.count(":") == 2:
            mac_str = mac.replace(":", "")
            mac_notation = "cisco"
            print(f"нотация {mac}: {mac_notation}")        
        else:
            print(f"нотация {mac} неизвестна")
    elif mac.find("-") == -1 and mac.find(":") == -1:
        mac_notation = "bare"
        print(f"нотация {mac}: {mac_notation}")




