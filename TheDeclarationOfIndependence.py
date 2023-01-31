# Programmer : Zachery Eckelbecker
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


# import Libraries here
import random
import time

# Gas level Function
def gaslevelGauge():
    gasLevelList = ["Empty","low","1/4 Tank","Half Tank","3/4 Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel


# Varibale calling gasLevelGuage function to store its value

gasLevelIndicator = gaslevelGauge()


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


