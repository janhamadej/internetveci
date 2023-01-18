import network

wlan = network.WLAN(network.STA_IF)

def do_connect():
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect('Nazov WIFI', 'Heslo Wifi')
        while not wlan.isconnected():
            pass
    print('NETWORK:', wlan.ifconfig())

do_connect()