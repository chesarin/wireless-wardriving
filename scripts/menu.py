#!/usr/bin/env python
def menu():
    print "Kismet XML logs analyser"
    print "Please choose an option:"
    print " "
    print "1) Find number of WEP networks"
    print "2) Find number of infrastructure networks"
    print "3) Find number of probe networks"
    print "4) Quit Kismet log analyser"
    print " "
    return input ("Choose your option: ")

def find_wep():
    print "inside of wep"

def find_infrastructure():
    print "inside infrastructure"

def find_probe():
    print "inside probe networks"

loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        find_wep()
    elif choice == 2:
        find_infrastructure()
    elif choice == 3:
        find_probe()
    elif choice == 4:
        loop = 0

print "Adios"
    
