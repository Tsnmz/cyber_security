#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("clear")
os.system("figlet VPN KONTROL")

print("""
\033[36mVPN Kontrol Aracımıza Hoş Geldiniz 
\033[33m---------------------------------
\033[33m 1) Vpn aracını çalıştır.
\033[33m 2) Aracı yeniden başlat
\033[33m 3) Menüye dön
\033[33m 4) Çık
\033[33m---------------------------------\033[0m

""")
print("""\033[31mNot\033[0m: Bu aracımız girmiş olduğunuz IP Adressinin 
bir VPN bağlantısına ait olup olmadığını göstermektedir. 

""")
islemno = raw_input("\033[36mİşlem Numarası Giriniz:\033[0m ")



if(islemno == "1"):
	hedefip = raw_input("Hedef IP Adressini Giriniz: ")
	os.system("ike-scan " + hedefip)
	print("""
	\033[33m---------------------------------
	\033[33m 1) Aracı yeniden başlat
	\033[33m 2) Menüye dön
	\033[33m 3) Çık
	\033[33m---------------------------------\033[0m
	""")
	islemno = raw_input("\033[36mİşlem Numarası Giriniz:\033[0m ")
	if(islemno == "1"):
		os.system("sudo python ./tools/VPN_Kontrol.py")
	
	elif(islemno == "2"):
		os.system("sudo python ./main.py")

	elif(islemno == "3"):
		os.system("clear")
		os.system("exit")
	else:
		os.system("sudo python ./tools/VPN_Kontrol.py")

elif(islemno == "2"):
	os.system("sudo python ./tools/VPN_Kontrol.py")
	
elif(islemno == "3"):
	os.system("sudo python ./main.py")

elif(islemno == "4"):
	os.system("clear")
	os.system("exit")
else:
	os.system("sudo python ./tools/VPN_Kontrol.py")
