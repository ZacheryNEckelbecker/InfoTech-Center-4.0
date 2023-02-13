# Programmer : Zachery Eckelbecker
# Date: 2.8.2023
# program: Infotech Center Upgrades

# import librarys here
import random 

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

