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
    time.sleep(0.0)
    if a == 4:
        a = 0
    if x == 20:
        print('Done!')

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




# Adding a program that gives you sigestions on your speed for how much sleep you got
sleep = int(input("How many hours of sleep did you get last night: "))

if sleep <= 1:
    print ("Please do not drive right now.")
elif sleep == 2 or 3 or 4:
    print ("\nPlease don't try to drive but if you have to drive 5 below the speed limit")
elif sleep == 5 or 6 or 7:
    print ("\nYou can drive normally just please be a little more aware of your seraoundings")
else:
    print ("you got a good amount of sleep, good for you")



# Adding a .random that will tell you when someone is in your blindspot

def blindspot():
    blindSpots = ("Left spot", "Right spot")
    inblindspot = random.choice(blindSpots)









# Create weather conditions in a list and choose them randomly 
def weather():
    weatherForcast = ["Snowing","Blizzard","Raining","Foggy","Windy","Icy","Sunshine"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition

# Variable to call weather() once our VRS
weatherAlert = weather()



# VRS() to respond to the weather condtions 
def vRS():
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
        print ("\nIts a sunny day, please still drive carfully")


def check_engine():
    engine_problems = ["spark plugs", "low oil pressure", "overheating engine", "oxygen sensor", "No Engine Problems"]
    print("Engine problem:", random.choice(engine_problems))


def check_transmission():
    transmission_problems = ["slipping transmission", "delayed engagement", "overheating transmission", "fluid leaks",
                             "No Transmission Problems"]
    print("Transmission problem: ", random.choice(transmission_problems))


def check_brakes():
    brake_problems = ["squeaky brakes", "Bad brake pedal", "low brake fluid", "No Brake Problems"]
    print("\nBrake problem: ", random.choice(brake_problems))


print("\nWhich part of the vehicle would you like to check?")
print("1. Engine")
print("2. Transmission")
print("3. Brakes")
print("4. No Part")

part_choice = input("Enter your choice (1, 2, 3, 4): ")

if part_choice == "1":
    while x != 50:
        x += 1
        b = ("Checking engine " + "." * a)
        a = a + 1
        sys.stdout.write('\r' + b)  # \r prints a carriage return first, so `b` is printed on top of the previous line.
        time.sleep(0.1)
        if a == 4:
            a = 0
        if x == 50:
            print('\n')
    check_engine()

elif part_choice == "2":
    while x != 60:
        x += 1
        b = ("Checking transmission " + "." * a)
        a = a + 1
        sys.stdout.write('\r' + b)  # \r prints a carriage return first, so `b` is printed on top of the previous line.
        time.sleep(0.1)
        if a == 4:
            a = 0
        if x == 60:
            print('\n')
    check_transmission()
elif part_choice == "3":
    while x != 70:
        x += 1
        b = ("Checking brakes " + "." * a)
        a = a + 1
        sys.stdout.write('\r' + b)  # \r prints a carriage return first, so `b` is printed on top of the previous line.
        time.sleep(0.1)
        if a == 4:
            a = 0
        if x == 70:
            print('\n')
    check_brakes()




#call fucntions here 
print ("National Weather service is checking condtion. ")
time.sleep(1)
vRS()
print ("Checking Current Gas Level")
time.sleep(1)
gaslevelAlert()
