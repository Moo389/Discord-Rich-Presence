import sys
from win10toast import ToastNotifier
import json
from colorama import Fore, init
import time
from pypresence import Presence, presence
import os

#            Hey listen if your seeing this i'm a shit coder thanks <3

config = json.load(open('config.json', 'rb'))

toaster = ToastNotifier()
toaster.show_toast("Cotra Rich Presence",
                   "Is now loading...",
                   icon_path="A.ico",
                   duration=10)

#            this just makes the notification (first time using so i'm not that good)


toaster.show_toast("Cotra Rich Presence",
                   "Is now loaded. Please wait 5 seconds",
                   icon_path="A.ico",
                   duration=5,
                   threaded=True)
while toaster.notification_active(): time.sleep(0.1)
def restart_bot(): 
  os.execv(sys.executable,sys.argv)

print(chr(27) + "[2J")

def Clear():
    os.system('cls')

rpc = Presence(config['Application'])
rpc.connect()
rpc.update(state=(config['State']),large_image=(config['largeimg']),start=time.time(),large_text=(config['large_text']),buttons=[{"label": (config['buttontext']), "url": (config['button_url'])}],small_image=(config['smallimg']),small_text=(config['smalltext']))


print("Cotra Rich Presence is now loaded! Please check discord")


print("Please Join discord.gg/cotraui for the cotraui selfbot.")

while True:
    time.sleep(699999)



#  Please make sure to join my server I'd much appreciate this <3