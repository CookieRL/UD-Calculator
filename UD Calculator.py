from os import system, name
from os import system
system("title " + "Ultimate Driving Calculator")

import colorama
from colorama import Fore
from colorama import Style
from colorama import init
init()
import time
def calculator():
	print("[+] Welcome to CookieRL's" + Fore.BLUE + Style.BRIGHT + " U" + Fore.RED + "D" + Style.RESET_ALL + " Calculator")
	
	time.sleep(1)
	print(Fore.YELLOW + "Use Underscores (_) in place of Commas ex 1,000 --> 1_000")
	print(Fore.BLUE + "[-] Insert Amount of Cash: " + Style.RESET_ALL)
	cash = input()

	print(Fore.BLUE + "[-] Insert Cash Per Mile: " + Style.RESET_ALL)
	mile = input()

	print(Fore.BLUE + "[-] Insert How much cash do you want?: " + Style.RESET_ALL)
	goal = input()

	cash = int(cash)
	mile = int(mile)
	goal = int(goal)

	amt = goal-cash

	amt = int(amt)

	print("Cash Remaining till Goal: " + Fore.GREEN + "{:,}".format(amt) + Style.RESET_ALL)
	cal1 = mile*7.3
	cal1 = int(cal1)
	race = amt//cal1
	race - int(race)
	mileage = amt//mile
	print("Amount of times to Drive from Nomtauk I-76 to South Beach I-76: " + Fore.GREEN + "{:,}".format(race))

	print("miles to go: ",mileage)

	input()
calculator()
