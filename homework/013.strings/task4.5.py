ip = "77.88.55.242"

ip = list(map(int, ip.split(".")))

ip.reverse()

ip_reversed = ".".join([str(oct) for oct in ip])

result = ip_reversed + ".in-addr.arpa"

print(result)
