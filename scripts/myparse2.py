#!/usr/bin/env python
from collections import defaultdict
import xml.etree.ElementTree as ET
tree = ET.parse('part-a.xml')
root = tree.getroot()
#for child in root:
#    print child.tag, child.attrib
counter = 0
counter2 = 0
securenetworks = defaultdict(int)
for networks in root.iter('wireless-network'):
    if len(networks):
        counter += 1
        networknumber = networks.get('number')
        networktype = networks.get('type')
        print 'network number: ', networknumber, 'network type: ',networktype
        for ssid in networks.findall('SSID'):
            if len(ssid):
                counter2 += 1
                essid = ssid.find('essid').text
                securessid = [ x.text for x in ssid.findall('encryption')]
                for x in securessid:
                    securenetworks[x] += 1
                print 'network number: ', networknumber, ' network name: ', essid,'network type: ',networktype
                print 'encryption: ', securessid 
#                for myencryption in ssid.findall('encryption'):
#                    print myencryption.text
#                print ssid.tag, ssid.attrib, essid

print "Total number of wireless-networks", counter
print "Total number of ssid in each network", counter2
for key in sorted(securenetworks):
    print key, '=>' , securenetworks[key]
#    myssid = ssid.find('essid').text
#    if myssid:
#        print myssid
