"""
Lecture 3 - Introduction into AI Programming with Python
@author: Dominik Jung (dominik.jung@jung-isec.de)
"""

data = {"Taycan" : "260 km/h", "Tesla" : "250 km/h"}

fobj = open("my_file.txt", "w")

for car in data:
    fobj.write("{}, {}\n".format(car, data[car]))
fobj.close()
