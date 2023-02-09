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

print (weatherAlert)
# VRS() to respond to the weather condtions 
def vRS():
    print


