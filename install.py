#!/usr/bin/env Python
# -*- coding: utf-8 -*-

import os 
os.system("clear")
os.system("sudo apt-get install figlet")
os.system("clear")
os.system("figlet ARAC KURULUMU")
print(""" 
 \033[31m-- Araçların kurulumunu yapmak için '1' değerini giriniz.
 \033[31m-- Eğer daha önce kurulum yaptıysanız '2' değerini girerek araçların bulunduğu menüye gidebilirsiniz!!!
 
  \033[31m GitHub: \033[36mhttps://github.com/Tsnmz
  \033[31m LinkedIn: \033[36mhttps://www.linkedin.com/in/tsnmz/
  \033[31m GitHub: \033[36mhttps://github.com/Tsnmz/cyber_security
 \033[0m""")
 
print(""" 
\033[36m           KURULUMA HOŞ GELDİNİZ\033[0m""")
print("\033[0m")
print("\033[32m---------------------------------------------")
print("""
\033[33m  1) Gerekli Dosyaları Kur. \033[31m(Gerekli dosyaları daha önce kurmadıysan araçlar çalışmıyacaktır.) 
\033[33m  2) Menüye Git
\033[33m  3) Çık
""")
print("\033[32m---------------------------------------------\033[0m")

islmno = raw_input("\033[32m1-3 Arasında Bir Sayı Giririniz:\033[0m ")
print("\033[0m")

islemno=0
if(islmno == "1"):
	os.system("sudo apt-get install nmap")
	os.system("sudo apt-get install chkrootkit")
	os.system("sudo apt-get install nikto")
	os.system("sudo apt-get install sqlmap")
	os.system("sudo apt-get install ike-scan")
	os.system("sudo apt-get install crucnh")
	os.system("sudo apt-get install wpscan")
	os.system("sudo apt-get install lynis")
	os.system("sudo apt-get install ncrack")
	os.system("sudo apt-get install wafw00f")
	os.system("sudo apt-get install macchanger")
	os.system("sudo apt-get install python")
	os.system("sudo ap-get install python3")
	os.system("clear")
	os.system("sudo python ./main.py")
	
elif(islmno == "2"):
	os.system("sudo python ./main.py")
	os.system("clear")

elif(islmno == "3"):
	os.system("clear")
	os.system("exit")
else:
	os.system("sudo python ./install.py")	
