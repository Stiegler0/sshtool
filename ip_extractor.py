import re
def extract_All_ips(sshlines):
    """
    take as arguement a list
    define patterns
    extract ip adresses, timestamp, type of connection (failed...)
    """
    matches = []
    ip_address_pattern = re.compile(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}') #xxx.xxx.xxx.xxx
    for i in sshlines:
        matches.extend(re.findall(ip_address_pattern,i))
    return(matches)