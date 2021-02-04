from urllib2 import urlopen
import re
res = urlopen('http://2ip.ru/').read()
print(re.search(b'\d+\.\d+\.\d+\.\d+', res).group())
