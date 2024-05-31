"""
.Nombre de tentatives échouées successives
.Taux de tentatives échouées par minute
.totale de tentative dans une durrée
"""

from datetime import datetime, timedelta

attempts_dict = {'192.168.0.34': 3, '192.168.0.35': 2, '192.168.0.32': 12}
failed = [
    {'failure_type': 'authentication failure', 'ip_address_source': '192.168.0.34', 'time': 'May 13 00:31:06'},
           {'failure_type': 'Failed password', 'ip_address_source': '192.168.0.34', 'port': '53222', 'time': 'May 13 00:31:08'},
             {'failure_type': 'Failed password', 'ip_address_source': '192.168.0.34', 'port': '53222', 'time': 'May 13 00:31:30'}]

# Totale de tentative dans une durrée:

def algo(ip,count_dict,failed,timetreshold):

    output = {'ip': ip, 'tim': [], 'nombre de tentatives': count_dict.get(ip,0)}
    timetreshold = timedelta(seconds=timetreshold)
    date_format = "%b %d %H:%M:%S"

    times = []
    for j in failed:
        if j["ip_address_source"] == ip:
            times.append(j["time"])
    #for j in failed:
     #   if(ip == j["ip_address_source"]):
      #     time.append(j["time"])

    times = [datetime.strptime(time,date_format) for time in times]
    times.sort()
    
    if times:
        start_time = times[0]
        end_time = start_time + timetreshold
        output['tim'] = [start_time.strftime('%Y-%m-%d %H:%M:%S')]

        for time in times[1:]:
            if time <= end_time:
                output['tim'].append(time.strftime('%Y-%m-%d %H:%M:%S'))


    print(f"dans {timetreshold}: {output['nombre de tentatives']}")
    return output
    #  debut_form = datetime.strptime(i,date_format)
    #   last_defined = debut_form + timetreshold

        #debut = time[0]
        #debut_form = datetime.strptime(debut, date_format)

    #for j in failed:
        #if(ip == j["ip_address_source"]):
        #   tim = j["time"]
        #    tim = datetime.strptime(tim,'%b %d %H:%M:%S')
       #     if tim <= last_defined:
      #          output["ip"] = ip
     #           output["tim"] = str(tim)


    #for i in attempts_dict:
    #   output["nombre de tentatives"] = attempts_dict.get(ip,0)
    #return output



test = algo('192.168.0.34',attempts_dict,failed,20)
print(test)


#{'ip': '192.168.0.32', 'durrée': '69 secondes', 'nombre de tentatives': 12}
