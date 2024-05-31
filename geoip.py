import ipinfo
# get the ip address from the command line
def locate(ip):

# access token for ipinfo.io
    access_token = '2679885b27caab'
# create a client object with the access token
    handler = ipinfo.getHandler(access_token)
# get the ip info
    details = handler.getDetails(ip)
    print(details.city)
# print the ip info
    for key, value in details.all.items():
        print(f"{key}: {value}")


loc = locate("109.12.210.78")
print(loc)