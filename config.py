basic = {
    "ServerIP": '125.227.141.116',  #Change to your IoTtalk IP or None for autoSearching
    "Reg_addr": None,               #None #if None, Reg_addr = MAC address
    "dm_name": 'Tano_Demo',         #Device Model Name
    "d_name": 'tano_demo_frame',    # None for autoNaming
}

idfs = [
    ('temperatures', float),
    ('atmosphericPressure', float),
    ('altitude', float),
    ('humidity', float),
    ('lightSensor', int),
    ('moisture', float),
]

odfs = [
    ('relay1', int),
    ('relay2', int),
    ('relay3', int),
]
