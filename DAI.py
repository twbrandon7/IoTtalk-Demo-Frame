import sys, time, DAN, requests, random
import config
import wrt_lib as wrt
from wrt_lib import client
from wrt_lib import LED_flash

ServerIP = config.basic["ServerIP"] #Change to your IoTtalk IP or None for autoSearching
Reg_addr = config.basic["Reg_addr"] #None #if None, Reg_addr = MAC address

odfs = config.odfs
idfs = config.idfs

DAN.profile['dm_name'] = config.basic["dm_name"]
DAN.profile['df_list'] = [name for (name, _) in (odfs+idfs)]
DAN.profile['d_name'] = config.basic["d_name"] # None for autoNaming
DAN.device_registration_with_retry(ServerIP, Reg_addr)
LED_flash(1)

reConnecting = False

while True:
    try:
        #Pull data
        for (name, t) in odfs:
            val = DAN.pull(name)
            wrt.transmission_led(True)
            if val != None:
                client.put(name, str(val[0]))
        wrt.transmission_led(False)

        #Push data
        for (name, t) in idfs:
            data = client.get(name)
            DAN.push(name, t(data))
            wrt.transmission_led(True)
        wrt.transmission_led(False)

        if reConnecting:
            LED_flash(1)
            reConnecting = False

    except Exception as e:
        print(e)
        if str(e).find('mac_addr not found:') != -1:
            print('Reg_addr is not found. Try to re-register...')
            DAN.device_registration_with_retry(ServerIP, Reg_addr)
        else:
            print('Connection failed due to unknow reasons.')
            reConnecting = True
            time.sleep(1)    

    time.sleep(0.2)
