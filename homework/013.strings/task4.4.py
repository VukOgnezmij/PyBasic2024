ip = "10.23.43.234"

ip = list(map(int, ip.split(".")))

result = ""

for oct in ip:
    result = result + format(oct,'08b')

print(result)