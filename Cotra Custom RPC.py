import os, sys, time, json

from colorama import Fore
from pypresence import Presence
from win10toast import ToastNotifier

config = json.load(open('config.json', 'rb'))

toaster = ToastNotifier()

print(chr(27) + "[2J")

rpc = Presence(config['Application'])
rpc.connect()
rpc.update(
    state = config['State'],
    large_image = config['largeimg'],
    start = time.time(),
    large_text = config['large_text'],
    buttons= [{
        "label": config['buttontext'],
        "url": config['button_url']
    }],
    small_image = config['smallimg'],
    small_text = config['smalltext']
)

toaster.show_toast(
    "Cotra Rich Presence",
    "Cotra RPC has loaded successfully!",
    icon_path="A.ico",
    duration=5,
    threaded=True
)

print(f"{Fore.CYAN}Please join {Fore.GREEN}discord.gg/cotraui{Fore.CYAN} for the CotraUI selfbot.")

while True:
    time.sleep(69420)

#  Please make sure to join my server I'd much appreciate this <3