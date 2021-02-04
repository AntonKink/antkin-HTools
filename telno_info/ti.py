from urllib2 import urlopen 
import json

phone = input("Enter phone: ")
getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + str(phone)

try:
    infoPhone = urlopen(getInfo)
except:
    print( "\n[!] - Phone not found - [!]\n" )

infoPhone = json.load(infoPhone)

print "Cellular number: ", phone
print "Country : ", infoPhone["country"]["name"]
print "Part of the light : ", infoPhone["country"]["location"]
print "Latitude: ", infoPhone["capital"]["latitude"]
print "Longitude: ", infoPhone["capital"]["longitude"]
print "Time Zone: ",infoPhone["capital"]["time_zone"]
