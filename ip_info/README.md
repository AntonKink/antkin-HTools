# Port-Scanner

## Some explanation
To begin with, let's decide what information we want to receive. Basically, it will be a city, country, continent (and suddenly) and a provider. It would also be nice to get whois information.   

## The work principle of the program
1. Take the IP address as input  
2. Create a URL by type: http://ipinfo.io/<IP>/json  
3. Request JSON data by contacting this address  
4. Change from JSON format to Python dictionary  
5. Using Python, run the command in the whois terminal <IP>  
6. Let's read the data from the paragraph above  
7. In a readable form, display the information received   
  
## How to use
```console
user@pc:~$ python ii.py
Enter IP: 89.***.***.***
------------------------------------------------------------
IP: 89.***.***.***
Hostname: ***
City: ***
Region: ***
Country: EE
Loc: ***
Org: ***
Postal: ***
TimeZone: ***
------------------------------------------------------------
% This is the RIPE Database query service.
% The objects are in RPSL format.
%
% The RIPE Database is subject to Terms and Conditions.
% See http://www.ripe.net/db/support/db-terms-conditions.pdf

... etc (lots of info) ...
 
```
