# Programmer : Zachery Eckelbecker
# Date: 1.28.2023
# program: Infotech Center Upgrades

"""
Our welcome screen will start our program letting drivers
know that the InfoTech Center 4.0 OS is loading
"""
# Import Libraries Here

import time
import sys


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



