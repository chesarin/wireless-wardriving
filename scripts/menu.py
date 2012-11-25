#!/usr/bin/env python
import xml.etree.ElementTree as ET
import os
from collections import defaultdict
path = 'xml_files'
dirList = os.listdir(path)

def menu():
    print "Kismet XML logs analyzer Options Menu"
    print "Please choose an option to execute:"
    print " "
    print "1) Find number of WEP networks"
    print "2) Find number of infrastructure networks"
    print "3) Find secure/insecure networks and encryption type"
    print "4) Find most common channels"
    print "5) Find vendors"
    print "6) Go back to previous menu"
    print " "
    return input ("Choose your option: ")

def find_wep(mytree):
    root = mytree.getroot()
    print "inside of wep"
    wepnet = []
    securenetworks = defaultdict(int)
    wepsentinel = 0
    totalnet = 0
    counter2 = 0
    for networks in root.iter('wireless-network'):
        if len(networks):
            totalnet += 1
            networknumber = networks.get('number')
            networktype = networks.get('type')
 #           print 'network number: ', networknumber, 'network type: ',networktype
            for ssid in networks.findall('SSID'):
                if len(ssid):
                    counter2 += 1
                    essid = ssid.find('essid').text
                    securessid = [ x.text for x in ssid.findall('encryption')]
                    for x in securessid:
                        if x == 'WEP':
                            wepnet.append(essid)
                            wepsentinel += 1
                        securenetworks[x] += 1
#                    print 'network number: ', networknumber, ' network name: ', essid,'network type: ',networktype
#                    print 'encryption: ', securessid 
#                for myencryption in ssid.findall('encryption'):
#                    print myencryption.text
#                print ssid.tag, ssid.attrib, essid
    print "Total number of networks ", totalnet
    print "Total number of secure networks ", counter2
    print "Total number of WEP networks found ", wepsentinel
    print "The following are those networks :"
    for i in wepnet:
        print i,
    print '\n'
#    print " "


def find_infrastructure(mytree):
    root = mytree.getroot()
    print "inside infrastructure"
    infrastructure = defaultdict(int)
    totalnet = 0
    for networks in root.iter('wireless-network'):
        if len(networks):
            totalnet += 1
            networknumber = networks.get('number')
            networktype = networks.get('type')
            infrastructure[networktype] += 1

    print 'Total number of networks', totalnet
    print 'Total size of dictionary', len(infrastructure)
    #Need to find out more about lambda
    for key, value in sorted(infrastructure.iteritems(), key=lambda (k,v): (v,k)):
        print 'type %s: occurrence %s' % (key, value)
    print " "

def find_most_common_channels(mytree):
    root = mytree.getroot()
    channels = defaultdict(int)
    totalnet = 0
    for networks in root.iter('wireless-network'):
        if len(networks):
            totalnet += 1
            networknumber = networks.get('number')
            networktype = networks.get('type')
            channel = networks.find('channel').text
            channels[channel] += 1

    print 'Total number of networks', totalnet
    print 'Total size of dictionary', len(channels)
    #Need to find out more about lambda
    for key, value in sorted(channels.iteritems(), key=lambda (k,v): (v,k)):
        print 'channel %s: occurrence %s' % (key, value)
    print " "

def find_most_popular_vendors(mytree):
    root = mytree.getroot()
    vendors = defaultdict(int)
    totalnet = 0
    for networks in root.iter('wireless-network'):
        if len(networks):
            totalnet += 1
            networknumber = networks.get('number')
            networktype = networks.get('type')
            vendor = networks.find('manuf').text
            vendors[vendor] += 1

    print 'Total number of networks', totalnet
    print 'Total size of dictionary', len(vendors)
    #Need to find out more about lambda
    for key, value in sorted(vendors.iteritems(), key=lambda (k,v): (v,k)):
        print 'vendor %s: occurrence %s' % (key, value)
    print " "
    
def find_secure_protocols(mytree):
    securenetworks = find_secure_networks(mytree)
    secureprotocols = defaultdict(int)
    for k, v in securenetworks.iteritems():
        for item in v:
            secureprotocols[item] += 1
    print 'Total size of dictionary', len(securenetworks)
    for key, value in sorted(secureprotocols.iteritems(), key=lambda (k,v): (v,k)):
        print 'encryption %s: occurrence %s' % (key, value)
    print " "


def find_secure_networks(mytree):
    print "inside find_secure_networks"
    root = mytree.getroot()
    securenetworks = {}
    totalnet = 0
    for networks in root.iter('wireless-network'):
        if len(networks):
            totalnet += 1
            networknumber = networks.get('number')
            networktype = networks.get('type')
            for ssid in networks.findall('SSID'):
                if len(ssid):
                    essid = ssid.find('essid').text
                    securessid = [ x.text for x in ssid.findall('encryption')]
                    securenetworks[essid] = securessid
    return securenetworks
#    print "Total number of networks : ", totalnet
#    print "Total secure networks : %d" % len(securenetworks)

#    for k, v in securenetworks.iteritems():
#        print k, v


def list_files():
    print "Kismet XML log analyser"
    print " "
    for idn, fname in enumerate(dirList):
        print idn, fname
    print len(dirList), "quit"
    print " "
    return input("Choose file to analyse: ")

def main2():
    loop = 1
    choice = 0
    while loop == 1:
        choice = list_files()
        if choice < len(dirList):
            xmlfile = path + '/' + dirList[choice]
            main(xmlfile)
        if choice > len(dirList):
            print "Invalid choice"
        elif choice == len(dirList):
            loop = 0

    print "Adios Amigo/Amiga"
    print "Thank You For Coming"


def main(xmlfile):
    tree = ET.parse(xmlfile)
    loop = 1
    choice = 0
    while loop == 1:
        choice = menu()
        if choice == 1:
            find_wep(tree)
        elif choice == 2:
            find_infrastructure(tree)
        elif choice == 3:
            find_secure_protocols(tree)
        elif choice == 4:
            find_most_common_channels(tree)
        elif choice == 5:
            find_most_popular_vendors(tree)
        elif choice == 6:
            loop = 0

    print "Adios"
    
if __name__ == '__main__':
    main2()
