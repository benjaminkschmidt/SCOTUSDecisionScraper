# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import nltk   
from urllib import urlopen
r = requests.get("https://caselaw.findlaw.com/court/us-supreme-court/volume")
r.content
soup = BeautifulSoup(r.content, "lxml")
print(soup.prettify())
#show all the href
volumes=[]

f = open("alllinks.txt", "w")

for link in soup.find_all("a"):
    volumes.append(link.get("href"))
print(volumes)
for i in volumes:
    
    f.write(i)
    f.write(", ")
f.close()
scotusFull=[]
for link in volumes:
    if "supreme" in link:
        if "volume" in link:
            scotusFull.append(link)
        else: 
            continue
    else: 
        continue
print(scotusFull)
f = open("allscotuslinks.txt", "w")
    
for i in scotusFull:
    
    f.write(i + '\n')
f.close()
#get each link set sublinks to get links for each case this will collect the links for each case
with open("allscotuslinks.txt") as linksfile:
    content = linksfile.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
count=0
for link in content:
    count+=1
    caseCount+=1
    cases=[]
    cleanvolume=[]
    r = requests.get(link)
    soup = BeautifulSoup(r.content, "lxml")
    for link in soup.find_all("a"):
        cases.append(link.get("href"))
    
    for link in cases:
        if "us-supreme-court" in link:
            if str(count) in link:
                cleanvolume.append(link)
        else: 
            continue
        print(cleanvolume)
    filename="volume"+str(count)+".txt"
    f1 = open(filename, "w")
    
    for i in cleanvolume:
    
        f.write(i + '\n')
    f1.close()
    for case in cleanvolume:
        

        url = str(case)   
        html = urlopen(url).read()    
        raw = nltk.clean_html(html)  
        filename="volume"+str(count)+"-"+str(caseCount)+".txt"
        f=open(filename,"w")
        f.write(raw)
        f.close
        caseCount+=1
#write each case to a file in a volume sized folder
#creates a file for each case/volume, need to check the tags
#get each link set sublinks to get links for each case this will collect the links for each case
with open("allscotuslinks.txt") as linksfile:
    content = linksfile.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 
count=0
for link in content:
    count+=1
    cases=[]
    cleanvolume=[]
    r = requests.get(link)
    soup = BeautifulSoup(r.content, "lxml")
    for link in soup.find_all("a"):
        cases.append(link.get("href"))
    
    for link in cases:
        if "us-supreme-court" in link:
            if str(count) in link:
                cleanvolume.append(link)
        else: 
            continue
        print(cleanvolume)
    filename="volume"+str(count)+".txt"
    f = open(filename, "w")
    
    for i in cleanvolume:
    
        f.write(i + '\n')
    f.close()

