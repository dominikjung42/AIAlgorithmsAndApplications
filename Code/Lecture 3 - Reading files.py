"""
Lecture 3 - Introduction into AI Programming with Python
@author: Dominik Jung (dominik.jung42@gmail.com)
"""

# Read local
fobj = open("database_extract.txt", "r")
for line in fobj:
    print(line)
fobj.close()

# Read local file into dictionnary
data = {}
fobj = open("database_extract.txt", "r")
for line in fobj:
    line = line.strip()
    l = line.split(",")
    data[l[0]] = l[1]
fobj.close()

# Final program
data = {}
fobj = open("database_extract.txt", "r")
for line in fobj:
    line = line.strip()
    l = line.split(",")
    data[l[0]] = l[1]
fobj.close()

while True: 
    car = input("Please enter a Porsche model: ")
    if car in data: 
        print("The car has the following VMax:", data[car]) 
    else: 
        print("Unknown Porsche model")

# Read from online
import urllib3
http = urllib3.PoolManager()
target_url = "https://raw.githubusercontent.com/dominikjung42/AIAlgorithmsAndApplications/master/Code/database_extract.txt"
response = http.request('GET', target_url)
data = response.data.decode('utf-8')








