#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-:-:-:-:-:-:-:-:-:-:-:-:#
#    Vaile Framework     #
#-:-:-:-:-:-:-:-:-:-:-:-:#

#Author : @_tID
#This module requires Vaile Framework
#https://github.com/VainlyStrain/Vaile


import time
from core.methods.tor import session
import socket
from core.Core.colors import *

info = "Find out where the target server is located."
searchinfo = "GeoIP Lookup"
properties = {}

def getgeoip(web):
    requests = session()
    web = web.replace('http://','')
    web = web.replace('https://','')
    if "@" in web:
        web = web.split("@")[1]
    #print(R+'\n   =========================')
    #print(R+'    G E O I P   L O O K U P')
    #print(R+'   =========================\n')
    from core.methods.print import posintpas
    posintpas("geoip lookup")
    time.sleep(0.4)
    print(GR+' [!] Looking Up for WhoIS Information...')
    time.sleep(0.4)
    print(GR+" [~] Found GeoIp Location: \n")
    domains = socket.gethostbyname(web)
    time.sleep(0.6)
    text = requests.get('http://api.hackertarget.com/geoip/?q=' + domains).text
    result = str(text)
    if 'error' not in result and 'invalid' not in result:
        res = result.splitlines()
        for r in res:
            print(O+' [+] ' + r.split(':')[0].strip() + ''+C+color.TR3+C+G+ r.split(':')[1].strip()+C+color.TR2+C)
            time.sleep(0.1)

    else:
        print(R+' [-] Outbound Query Exception!')
        time.sleep(0.8)

def attack(web):
    getgeoip(web)