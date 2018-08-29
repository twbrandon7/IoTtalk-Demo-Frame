import os, sys
sys.path.insert(0, '/usr/lib/python2.7/bridge/')  
from bridgeclient import BridgeClient  

client = BridgeClient()

def LED_flash(LED_state):
    if LED_state:
        client.put('Reg_done', '1')
        os.system(r'echo "timer" > /sys/class/leds/ds:green:usb/trigger')      #For ArduinoYun Only. LED Blink.
    else:
        client.put('Reg_done', '0')
        os.system(r'echo "none" > /sys/class/leds/ds:green:usb/trigger')

def transmission_led(on=True):
    if on:
        os.system(r'echo "default-on" > /sys/class/leds/ds:green:wlan/trigger')
    else:
        os.system(r'echo "none" > /sys/class/leds/ds:green:wlan/trigger')