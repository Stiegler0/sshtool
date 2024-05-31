def parse_log(lines):
    """
    define regex to extact all lines that are related to ssh 
    return a new file (only ssh informations)
    """
    ssh_lines = []
    for line in lines:
        if 'ssh'  in line or 'sshd' in line:
            ssh_lines.append(line.strip())
    return ssh_lines