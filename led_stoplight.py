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