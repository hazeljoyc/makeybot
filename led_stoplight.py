# ============================================================================
# Source: STEAM Clown - www.steamclown.org 
# GitHub: https://github.com/hazeljoyc/makeybot
# Hacker: Hazel Joy Chavez
# This example code is licensed under the CC BY-NC-SA 4.0, GNU GPL and EUPL
# https://creativecommons.org/licenses/by-nc-sa/4.0/
# https://www.gnu.org/licenses/gpl-3.0.en.html
# https://eupl.eu/
# Program/Design Name:        led_stoplight.py
# Description:    This is a program to turn on and off a set of 3 LEDs.
# program description:
# 1) Read values from traffic_light library
# 2) Check status of each light
# 3) Turn on light depending on value
# Dependencies:   python3
# ============================================================================

from gpiozero import LED
import time

traffic_light = {'red_led' : [0,3], 'yellow_led' : [0,27], 'green_led' : [0,13]}
        

def display_light(lights):
    for status in traffic_light.values():
        light_status = status[0]
        light = LED(status[1])
        if light_status == 0:
            status[0] = 1
            light.on()
        else:
            status[0] = 0
            light.off()
        time.sleep(1)
            
            
def main():
    while(True):
        display_light(traffic_light)
        
main()
