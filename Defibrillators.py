"""
The Goal
The city of Montpellier has equipped its streets with defibrillators to help save victims of cardiac arrests. The data corresponding to the position of all defibrillators is available online.

Based on the data we provide in the tests, write a program that will allow users to find the defibrillator nearest to their location using their mobile phone.
 
Rules
The input data you require for your program is provided in text format.
This data is comprised of lines, each of which represents a defibrillator. Each defibrillator is represented by the following fields:
A number identifying the defibrillator
Name
Address
Contact Phone number
Longitude (degrees)
Latitude (degrees)
"""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
min, loc = None, None
lon = float(input().replace(',','.'))
lat = float(input().replace(',','.'))
n = int(input())
for i in range(n):
    defib = input()
    # Process the string to get longitude and latitude
    dlon = float((defib.split(';')[4]).replace(',','.'))
    dlat = float((defib.split(';')[5]).replace(',','.'))
    # calculate distance to the defib
    x = (dlon - lon) * math.cos(lat + dlat /2)
    y = dlat - lat
    d = math.sqrt(x**2 + y**2) * 6371
    # if closer then previous defib, set as new closest
    if (min == None) or (min > d):
        loc = defib.split(';')[1]
        min = d
        
print(loc)
