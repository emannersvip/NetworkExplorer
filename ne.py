#!/usr/bin/python3

#import subprocess
path = "/home/emanners/Documents/Code/NetworkExplorer/"

# https://learnpython.com/blog/custom-class-python/
class Nethost:
    def __init__(self, hostip, hostname) -> None:
        self.hostip = hostip
        self.hostname = hostname

arptable = open(path + "arpTable.txt", "r")
arpArray = arptable.readlines()
nodeArray = []

print("\n")
#print(arpArray[3])

# Example populate newly instantiated Nethost
#four_u = Nethost("192.168.1.86", "Threeleaf-4u.edsonmanners.com")
#print(four_u.hostip)

for node in arpArray:

    tmpip = node.split(" ")[1]
    tmpname = node.split(" ")[0]
    
    # Check and sanitize data
    # Remove first and last chars... Parenthesis.
    tmpip = tmpip[:-1]
    tmpip = tmpip[1:]
    
    # If hostname is missing '?' change ot unknown
    #bob = Nethost(tmpip, tmpname)
    #print(tmpip)
    #print(bob.hostip + " : " + bob.hostname)
    nodeArray.append(Nethost(tmpip, tmpname))

for entry in nodeArray:
    print(entry.hostip + " <==> " + entry.hostname)