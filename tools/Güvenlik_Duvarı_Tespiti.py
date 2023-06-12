#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("clear")
os.system("figlet Guvenlik Duvari Tespiti")

print("""
Güvenlik Duvarı Tespiti Etme Aracına Hoş Geldiniz

""")
site = raw_input("Site Adresini Giriniz: ")

os.system("sudo wafw00f " + site)

print("""
\033[33m---------------------------------
\033[33m 1) Aracı yeniden başlat
\033[33m 2) Menüye Dön\033
\033[33m 3) Çık\033[0m
\033[33m---------------------------------
""")

islemno = raw_input("\033[32mLütfen bir değer giriniz:\033[0m ")
if(islemno == "1"):
	os.system("sudo python ./tools/Güvenlik_Duvarı_Tespiti.py")
	
elif(islemno == "2"):
	os.system("sudo python ./main.py")

elif(islemno == "3"):
	os.system("clear")
	os.system("exit")
else:
	os.system("sudo python ./tools/Güvenlik_Duvarı_Tespiti.py")
