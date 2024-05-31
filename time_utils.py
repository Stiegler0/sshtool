from collections import defaultdict
from datetime import datetime, date

def time_check_susIps(journal):

    grouped_connections = defaultdict(list)
    global_output = {}
    for connection in journal:
        ip = connection['ip_address']
        grouped_connections[ip].append(connection)
    for ip_address, group in grouped_connections.items():
        print(f"Adresse IP : {ip_address}")
        for connection in group:
            print(f" - time : {connection['time']}, Status : {connection['failure_type']}")
        print()  
    for ip_address, log in grouped_connections.items():
        first_time = None
        last_time = None
        count_of_attempts = 0
        for i in log:
            count_of_attempts +=1
            timestamp_entry = i["time"]
            if first_time is None or timestamp_entry < first_time:
                first_time = timestamp_entry
            if last_time is None or timestamp_entry > last_time:
                last_time = timestamp_entry
            if first_time == last_time:
                output = {}
                output["seule tentative:"] = first_time
                
            else:
                output = {}
                output["première tentative:"] = first_time
                output["dernière tentative:"] = last_time
                
                
        print(f"pour l'adresse: {ip_address}: ")
        print(f" - Times : {output}")

        count = len(output.keys())

        if count == 1:
            print(" - seule tentative xD")
        elif count == 2:
            annee = date.today().year
            debut = output["première tentative:"]
            debut_formated = datetime.strptime(f"{debut} {annee}", '%b %d %H:%M:%S %Y')
            fin = output["dernière tentative:"]
            fin_formated = datetime.strptime(f"{fin} {annee}", '%b %d %H:%M:%S %Y')
            duree = fin_formated - debut_formated
            total_seconds = int(duree.total_seconds())
            days, reste = divmod(total_seconds,86400)
            hours, reste = divmod(reste,3600)
            minutes, reste = divmod(reste,60)
            human_readable_duration = []

            if days > 0:
                human_readable_duration.append(f"{days} jour{'s' if days >1 else ''}")
            if hours >0:
                human_readable_duration.append(f"{hours} heure{'s' if hours > 1 else ''}")
            if minutes>0:
                human_readable_duration.append(f"{minutes} minute{'s' if minutes > 1 else ''}")
            if total_seconds > 0 or not human_readable_duration:
                human_readable_duration.append(f"{total_seconds} seconde{'s' if total_seconds != 1 else ''}")

            human_readable_duration_str =' '.join(human_readable_duration)
            print(f" - Duration: {human_readable_duration_str}")
            print(f" - {count_of_attempts} tentative{'s' if count_of_attempts > 1 else ''} en {human_readable_duration_str}")
            print()
    return human_readable_duration_str  



def time_interval_for_exactIP(ip,count_dict,journal):
    output = {}
    time = []
    annee = date.today().year

    for j in journal:
        if(ip == j["ip_address_source"]):
           time.append(j["time"])

    for y in time:
        debut = time[0]
        cmt = len(time)
        last = time[cmt - 1]

    debut_formated = datetime.strptime(f"{debut} {annee}", '%b %d %H:%M:%S %Y')
    output["ip"] = ip
    fin_formated = datetime.strptime(f"{last} {annee}", '%b %d %H:%M:%S %Y')
    durre = fin_formated - debut_formated
    output["durrée"] = f"{int(durre.total_seconds())} secondes"


    for i in count_dict:
        output["ip"] = ip
        output["nombre de tentatives"] = count_dict.get(ip,0)
            
    return output
