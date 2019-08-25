# This is script that run when device boot up or wake from sleep.
import network
#from components import blinker  #optionally - blink about status
# noinspection PyUnresolvedReferences
from system import utelnetserver
# noinspection PyUnresolvedReferences
from system import uftpd    #start FTP server

sta_if = network.WLAN(network.STA_IF);
sta_if.active(True)
sta_if.connect("YOUR-WIFI-SSID", "YOUR_PASSWORD")
if sta_if.isconnected():
    print("Connected to WiFi")
    print(sta_if.ifconfig())    #prinf network settings
    utelnetserver.start()       #start the Telnet server
#    blinker.blink_connected_to_wifi()  #optionally - blink with specific pattern about successful connection
else:
    print("Not connected to WiFi")
    # blinker.blink_not_connected_to_wifi()  #optionally - blink with specific pattern about failed connection
