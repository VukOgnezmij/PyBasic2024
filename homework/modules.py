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

def validateIP(inputIP):
    if len(inputIP) != 4:
        return False
    for part in inputIP:
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