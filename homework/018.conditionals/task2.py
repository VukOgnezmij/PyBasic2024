ip = "234.3.2.1"

ip_list = ip.split(".")
first_oct = int(ip_list[0])
if first_oct in range(1,127):
    ip_class = "A"
elif first_oct in range(128,191):
    ip_class = "B"
elif first_oct in range(192,223):
    ip_class = "C"
elif first_oct in range (224,239):
    ip_class = "D"
else: 
    ip_class = "E"
ip = ".".join([str(oct) for oct in ip_list])

print(f"класс ip {ip}: {ip_class}")