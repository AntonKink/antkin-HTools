from urllib2 import urlopen
import json
import os

getIP = raw_input("Enter IP: ")
url = "https://ipinfo.io/" + str(getIP) + "/json"

try:
    getInfo = urlopen(url)

except:
    print( "\n[!] - IP not found! - [!]\n" )

infoList = json.load(getInfo)

def whoisIPinfo(ip):

    try:

        myComand = "whois " + getIP
        whoisInfo = os.popen( myComand ).read()
        return whoisInfo

    except:

        return "\n [!] -- Error -- [!] \n"

print( "-" * 60 )

print("IP: " + infoList["ip"])
print("Hostname: " + infoList["hostname"])
print("City: " + infoList["city"])
print("Region: " + infoList["region"])
print("Country: " + infoList["country"])
print("Loc: " + infoList["loc"])
print("Org: " + infoList["org"])
print("Postal: " + infoList["postal"])
print("TimeZone: " + infoList["timezone"])

print( "-" * 60 )
print( whoisIPinfo ( getIP ) )
print( "-" * 60)


