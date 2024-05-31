# main.py

from file_reader import read_file
from log_parser import parse_log
from ip_extractor import extract_All_ips
from connection_analyzer import failed_connections, detect_sus_ip, total_failed_attempts
from time_utils import time_check_susIps, time_interval_for_exactIP
from reputation_score import number_failed_attempts_Indicative
if __name__ == "__main__":
    lines = read_file("/home/stiegler/my_tool/src/first.txt")
    ssh_lines = parse_log(lines)
    ips = extract_All_ips(ssh_lines)

    failed = failed_connections(ssh_lines)
    result, result_list = detect_sus_ip(failed)
    print(ips)
    #print(result)
    
    ip_attempts = total_failed_attempts(result_list)
    #print(ip_attempts)
    
    time_intervals = time_check_susIps(result_list)
    print(time_intervals)
    
    specific_ip_interval = time_interval_for_exactIP('192.168.0.34', ip_attempts, failed)
    #print(specific_ip_interval)
    duration = specific_ip_interval["durrée"]
    #print(type(duration))
    duration = duration.strip("secondes")
    #print(duration)
