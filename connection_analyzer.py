import re
from collections import defaultdict
from datetime import datetime

def failed_connections(lines):
    list_of_failed_logs = []
    ip_pattern = re.compile(r'from (\S+) port')
    ip_pattern2 = re.compile(r'rhost=(\d+\.\d+\.\d+\.\d+)')
    port_pattern = re.compile(r'port (\S+) ssh.')
    time_pattern = re.compile(r'(\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})')
    for line in lines:
        log_info = {}
        if "Failed password for" in line:
            log_info["failure_type"]= "Failed password"
            log_info['ip_address_source'] = ip_pattern.search(line).group(1)
            log_info['port'] = port_pattern.search(line).group(1)
            log_info['time'] = time_pattern.search(line).group(0)
            list_of_failed_logs.append(log_info)
        elif "authentication failure" in line:
            log_info["failure_type"]= "authentication failure"
            log_info['ip_address_source'] = ip_pattern2.search(line).group(1)
            log_info['time'] = time_pattern.search(line).group(0)
            list_of_failed_logs.append(log_info)
    return list_of_failed_logs




def detect_sus_ip(failed_connections):
    """
    took  list returned by failed connections, check is there an idress ip occurs many times
    then anchuf dik ip address li kat3awd f chhal intervalle dyal w9t
    """
    ip_address_counts = {}
    result_list = []
    for log in failed_connections:
        ip_address = log['ip_address_source']
        time = log['time']
        failure_type = log['failure_type']
        if ip_address in ip_address_counts:
            ip_address_counts[ip_address] += 1
        else:
            ip_address_counts[ip_address] = 1
        result_list.append({'ip_address': ip_address, 'time':time, 'failure_type':failure_type})
    for ip_address, count in ip_address_counts.items():
        if count >1:
            result = f'{ip_address}: {count} occurs times'
    return result, result_list


def total_failed_attempts(journal):
    ip_count ={}
    for i in journal:
        ip_address = i["ip_address"]
        if ip_address in ip_count:
            ip_count[ip_address] +=1
        else:
            ip_count[ip_address] = 1

    
    return ip_count