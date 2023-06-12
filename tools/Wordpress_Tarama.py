#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.system("clear")
os.system("figlet WORDPRESS TARAMA")


print("""
\033[36mWordpress Tarama Programına Hoş Geldiniz. 

\033[33m---------------------------------
\033[33m 1) Hızlı Tarama
\033[33m 2) Eklenti Tarama
\033[33m 3) Tema Tarama
\033[33m 4) Yönetici Kullanıcı Adı Tarama
\033[33m 5) Aracı yeniden başlat
\033[33m 6) Menüye dön
\033[33m 7) Çık
\033[33m---------------------------------\033[0m	
""")
islemno = raw_input("\033[36mİşlem Numarası Giriniz:\033[0m ")

if(islemno=="1"):
	site = raw_input("Site Adresi Girin: ")
	os.system("sudo wpscan --url " + site)
	print("""
	\033[33m---------------------------------
	\033[33m 1) Aracı yeniden başlat
	\033[33m 2) Menüye dön
	\033[33m 3) Çık
	\033[33m---------------------------------\033[0m
	""")
	islemno = raw_input("\033[36mİşlem Numarası Giriniz:\033[0m ")
	if(islemno == "1"):
		os.system("sudo python ./tools/Wordpress_Tarama.py")
	
	elif(islemno == "2"):
		os.system("sudo python ./main.py")

	elif(islemno == "3"):
		os.system("clear")
		os.system("exit")
	else:
		os.system("sudo python ./tools/Wordpress_Tarama.py")

elif(islemno == "2"):
	site = raw_input("Site Adresi Girin: ")
	os.system("sudo wpscan --url " + site + " --enumerate p")
	print("""
	\033[33m---------------------------------
	\033[33m 1) Aracı yeniden başlat
	\033[33m 2) Menüye dön
	\033[33m 3) Çık
	\033[33m---------------------------------\033[0m
	""")
	islemno = raw_input("\033[36mİşlem Numarası Giriniz:\033[0m ")
	if(islemno == "1"):
		os.system("sudo python ./tools/Wordpress_Tarama.py")
	
	elif(islemno == "2"):
		os.system("sudo python ./main.py")

	elif(islemno == "3"):
		os.system("clear")
		os.system("exit")
	else:
		os.system("sudo python ./tools/Wordpress_Tarama.py")

elif(islemno == "3"):
	site = raw_input("Site Adresi Girin: ")
	os.system("sudo wpscan --url " + site + " --enumerate t")
	print("""
	\033[33m---------------------------------
	\033[33m 1) Aracı yeniden başlat
	\033[33m 2) Menüye dön
	\033[33m 3) Çık
	\033[33m---------------------------------\033[0m
	""")
	islemno = raw_input("\033[36mİşlem Numarası Giriniz:\033[0m ")
	if(islemno == "1"):
		os.system("sudo python ./tools/Wordpress_Tarama.py")
	
	elif(islemno == "2"):
		os.system("sudo python ./main.py")

	elif(islemno == "3"):
		os.system("clear")
		os.system("exit")
	else:
		os.system("sudo python ./tools/Wordpress_Tarama.py")

elif(islemno == "4"):
	site = raw_input("Site Adresi Girin: ")
	os.system("sudo wpscan --url " + site + " --enumerate u")
	print("""
	\033[33m---------------------------------
	\033[33m 1) Aracı yeniden başlat
	\033[33m 2) Menüye dön
	\033[33m 3) Çık
	\033[33m---------------------------------\033[0m
	""")
	islemno = raw_input("\033[36mİşlem Numarası Giriniz:\033[0m ")
	if(islemno == "1"):
		os.system("sudo python ./tools/Wordpress_Tarama.py")
	
	elif(islemno == "2"):
		os.system("sudo python ./main.py")

	elif(islemno == "3"):
		os.system("clear")
		os.system("exit")
	else:
		os.system("sudo python ./tools/Wordpress_Tarama.py")

elif(islemno == "5"):
	os.system("sudo python ./tools/Wordpress_Tarama.py")
	
elif(islemno == "6"):
	os.system("sudo python ./main.py")

elif(islemno == "7"):
	os.system("clear")
	os.system("exit")
else:
	os.system("sudo python ./tools/Wordpress_Tarama.py")
