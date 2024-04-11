def print_output(p_host,p_network,p_wildcard,p_broadcast,p_host_min,p_host_max,p_cidr):
    print("Host: " + '/'.join([str(data) for data in p_host]))
    print("Network: " + '.'.join([str(oct) for oct in p_network]))
    print("Wildcard: " + '.'.join([str(oct) for oct in p_wildcard]))   
    print("Broadcast: " + '.'.join([str(oct) for oct in p_broadcast]))
    print("Host Min: " + '.'.join([str(oct) for oct in p_host_min]))   
    print("Host Max: " + '.'.join([str(oct) for oct in p_host_max]))
    print("CIDR: " + str(p_cidr))
    print("\n")

def wrongData(wrong_data):
    print("Wrong input: " + '.'.join([str(d) for d in wrong_data]) + '\n')
    
def wrongHost(bad_host):
    print("Wrong input: " + '/'.join([str(d) for d in bad_host]) + '\n')

def OnesOnTheLeft(part):
    return ((part+1) & part == 0) and (part!=0)

def hostIsDigit(d_host):
    for d_host_part in d_host:
        d_host_part = d_host_part.replace(".", "")
        if not str(d_host_part).isdigit():
            return False
    return True        

def validateIP(input):
    if len(input) != 4:
        return False
    for part in input:
        if part < 0 or part > 255:
            return False
    return True

def validateMask(inputMask):
    if len(inputMask) != 4:
        return False
    for partMask in inputMask:
        if partMask < 0 or partMask > 255:
            return False
        if "01" in str(bin(partMask)[2:]):
            return False 
    return True

homework_task = ["192.168.63.54 / 255.255.254.0", "192.168.43.54 / 255.255.255.240"] 
#homework_task = ["192.168.63.54 /     255.255.254.0"]
for host in homework_task:
    host = host.replace(" ", "")
    host = host.split("/")
    if hostIsDigit(host) == True:
        ip = list(map(int, host[0].split(".")))
        if validateIP(ip) == True:
            mask = list(map(int, host[1].split(".")))
            if validateMask(mask) == True:
                cidr = sum([bin(int(bits)).count("1") for bits in mask])
                if cidr < 31 :
                    network = [i & m for i,m in zip(ip, mask)]
                    wildcard = [255^m for m in mask]
                    broadcast = [(i | ~m) & 0xff for i, m in zip(ip, mask)]
                    host_min = network[:]
                    host_max = broadcast[:]
                    host_min[3] = host_min[3] + 1
                    host_max[3] = host_max[3] - 1
                    print_output(host,network,wildcard,broadcast,host_min,host_max,cidr)
                elif cidr == 31 :
                    network = [i & m for i,m in zip(ip, mask)]
                    wildcard = [255^m for m in mask]
                    broadcast = [(i | ~m) & 0xff for i, m in zip(ip, mask)]
                    host_min = network[:]
                    host_max = broadcast[:]
                    print_output(host,network,wildcard,broadcast,host_min,host_max,cidr)
                else:
                    print(host[0] + " is Localhost" + '\n')
            else:
                wrongData(mask)
        else:
            wrongData(ip)
    else:
        wrongHost(host)
    
        
    
    

