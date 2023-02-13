# Programmer: Zachery Eckelbecker
# 2/6/23
# Merged Welcome Screen and Gasoline Branches - Stable




# Programmer : Zachery Eckelbecker
# Date: 2.8.2023
# program: Infotech Center Upgrades

"""
Our welcome screen will start our program letting drivers
know that the InfoTech Center 4.0 OS is loading
"""
# Import Libraries Here

import sys
import random
import time


x = 0
a = 0

while x != 20:
    x += 1
    b = ("\033[31m[\Welcome - InfoTech 4.0 OS is Loading" + "." * a)
    a = a + 1
    sys.stdout.write('\r'+b) # \r prints a carriage return first, so `b` is printed on top of the previous line.
    time.sleep(0.25)
    if a == 4:
        a = 0
    if x == 20:
        print('\033[31m[1;32;40m Done!')

from time import sleep



print ("\n\nWelcome - InfoTech 4.0 OS is Loading")
sleep(1)










# Date: 1.30.2023
# program: Infotech Center 4.0 Gasoline

"""
We will create a Function that will tell us our fuel gauge level
    - Create a List with Gas Levels
    - Randomize and choose from the list to determine our gas level

Create a function to determine our closest gas station
    -Create a list of gas startions
    -Randomly choose a gas station from the list

Create a Function to determine our gas level and closest gas station
    -Print gas level
    -Print Closest Gas Station
"""



# Gas level Function
def gaslevelGauge():
    gasLevelList = ["Empty","low","1/4 Tank","Half Tank","3/4 Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel


# Varibale calling gasLevelGuage function to store its value

gasLevelIndicator = gaslevelGauge()
print ("  ")


# Gas Station Function
def closestGasStation():
    gasStations = ["Shell","Sams Club","Costco","Buc-ee's","7 Eleven","speedway","Circle-K","Meijer","Marathon"]
    closestGasStations = random.choice(gasStations)
    return closestGasStations


# Determine gas level & closest gas station
def gaslevelAlert():
    milesToLow = round(random.uniform(1,25),2)
    milesToGasStationQuartTank = round(random.uniform(26, 50), 2)
    if gasLevelIndicator == "Empty":
        print ("*** WARNING GAS LEVEL IS EMPTY***")
        time.sleep(1)
        print ("Calling Emergency Contact")
    elif gasLevelIndicator == "low":
        print (" ***Warning*** Gas tank is extremely low")
        time.sleep(.5)
        print ("Finding closest gas station")
        time.sleep(.5)
        print ("The closest gas station is", closestGasStation(), "which is", milesToLow, "miles away")
    elif gasLevelIndicator == "1/4 Tank":
        print ("***Warning***")
        time.sleep(1)
        print ("Your gas tank is at a 1/4 tank and the closest Gas Station is", closestGasStation(),"which is", milesToLow)
    elif gasLevelIndicator == "Half Tank":
        print ('Your gas tank is half full, you should have time to get to your destination.')
    elif gasLevelIndicator == "3/4 Tank":
        print (" Your gas tank is at 3/4, you have time to make it to your destination")
    else:
        print ("Your gas tank is full, no need to do anything")

gaslevelAlert()




# Create weather conditions in a list and choose them randomly 
def weather():
    weatherForcast = ["Snowing","Blizzard","Raining","Foggy","Windy","Icy","Sunshine"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition

# Variable to call weather() once our VRS
weatherAlert = weather()



# VRS() to respond to the weather condtions 
def vRS():
    print
    if weatherAlert == "Snowing":
        print ("\nNational Weather service has changed your alarm by 15 minutes because of th weather forcest of",weatherAlert)
        print ("your VRS has been ingaed only allowing your vehicle to go 45 MPH")
    elif weatherAlert == "Blizzard":
        print ("\nNational Weather service has changed your alarm by 40 minutes because of th weather forcest of",weatherAlert)
        print ("your VRS has been ingaed only allowing your vehicle to go 30 MPH")
    elif weatherAlert == "Raining":
        print ("\nNational Weather service is calling to inform you that is it",weatherAlert,"Please be more careful when driving")
    elif weatherAlert == "Foggy":
        print ("\nNational Weather service is calling to inform you that is it",weatherAlert,"Please be more careful when driving")
    elif weatherAlert == "Windy":
        print ("\nNational Weather service is calling to inform you that is it",weatherAlert,"Please be more careful when driving in a larger car")
    elif weatherAlert == "Icy":
        print ("\nNational Weather service has changed your alarm by 65 minutes because of th weather forcest of",weatherAlert)
        print ("your VRS has been ingaed only allowing your vehicle to go 25 MPH")
    else:
        print ("Its a sunny day, please still drive carfully")
vRS()


