#!usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.system("clear")
os.system("figlet Sunucu Zafiyet Analizi")

print("""\033[36mSunucu Zafiyet Analizi Aracına Hoş Geldiniz 
\033[33m---------------------------------
\033[33m 1) Zafiyet Analizini Başlat
\033[33m 2) Aracı yeniden başlat
\033[33m 3) Menüye Dön
\033[33m 4) Çık\033[0m
\033[33m---------------------------------
\033[0m""")

islemno = raw_input("\033[36mİşlem Numarası Giriniz:\033[0m ")

 
if(islemno == "1"):
	hedefip = raw_input("Hedef IP Adresinizi Giriniz: ")
	os.system("sudo nikto -h " + hedefip)
	
elif(islemno == "2"):
	os.system("sudo python ./tools/Sunucu_Zafiyet_Aracı.py")
	
elif(islemno == "3"):
	os.system("sudo python ./main.py")

elif(islemno == "4"):
	os.system("clear")
	os.system("exit")
else:
	os.system("sudo python ./tools/Sunucu_Zafiyet_Aracı.py")
