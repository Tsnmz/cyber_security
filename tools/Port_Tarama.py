#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


os.system("clear")
os.system("figlet PORT TARAMA")

print("""\033[36mPort Tarama Programına Hoş Geldiniz 
\033[33m---------------------------------
\033[33m 1) Hızlı Tarama
\033[33m 2) Servis ve Verisyon Bilgisi
\033[33m 3) İşletim Sistemi Bilgisi
\033[33m 4) Aracı yeniden başlat
\033[33m 5) Menüye Dön
\033[33m 6) Çık\033[0m
\033[33m---------------------------------
\033[0m""")

islemno = raw_input("\033[36mİşlem Numarası Giriniz:\033[0m ")

if(islemno == "1"):
	   hedefip = raw_input(" Hedef İp Giriniz: ")
	   os.system("sudo nmap " + hedefip)
elif(islemno == "2"):
	   hedefip = raw_input(" Hedef İp Giriniz: ")
	   os.system("sudo nmap -sS -sV " + hedefip)
elif(islemno == "3"):
	   hedefip = raw_input(" Hedef İp Giriniz: ")
	   os.system("sudo nmap -O " + hedefip)
elif(islemno == "4"):
	os.system("sudo python ./tools/Port_Tarama.py")
	
elif(islemno == "5"):
	os.system("sudo python ./main.py")

elif(islemno == "6"):
	os.system("clear")
	os.system("exit")
else:
	os.system("sudo python ./tools/Port_Tarama.py")
