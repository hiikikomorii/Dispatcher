import time
from colorama import init, Fore
import platform
import psutil
import socket
from pynput.keyboard import Controller, Key

init(autoreset=True)
keyboard = Controller()

keyboard.press(Key.f11)
keyboard.release(Key.f11)
time.sleep(0.5)

def clear():
    print("\n" * 2)

print(f"{Fore.LIGHTCYAN_EX}System: \n")
print(f"{Fore.LIGHTBLUE_EX}OS: {platform.system()}")
print(f"{Fore.LIGHTBLUE_EX}Version: {platform.machine()}")
print(f"{Fore.LIGHTBLUE_EX}Name: {platform.node()}")
print(f"{Fore.LIGHTBLUE_EX}IP: {socket.gethostbyname(socket.gethostname())}")
print(f"{Fore.LIGHTBLUE_EX}Python version: {platform.python_version()}")
print(f"{Fore.LIGHTBLUE_EX}Cores: {psutil.cpu_count()}")
clear()

while True:
    print(Fore.LIGHTBLUE_EX + "1 - auto     2 - manual control")
    choiice = input("> ")
    if choiice == "1":
        while True:
            print(f"{Fore.LIGHTBLUE_EX}CPU: {psutil.cpu_percent(interval=1)}%")
            mem = psutil.virtual_memory()
            print(f"{Fore.LIGHTBLUE_EX}RAM: {mem.percent}%")
            clear()
            time.sleep(1)

    elif choiice == "2":
        while True:
            input("> ")
            print(f"{Fore.LIGHTBLUE_EX}CPU: {psutil.cpu_percent(interval=1)}%")
            mem = psutil.virtual_memory()
            print(f"{Fore.LIGHTBLUE_EX}RAM: {mem.percent}%")
            clear()

    else:
        print(Fore.RED + "please choice number")