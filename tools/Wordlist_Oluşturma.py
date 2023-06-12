#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("clear")
os.system("figlet WordList Olusturma")


print("""\033[36mWordlist Oluşturma Aracına Hoş Geldiniz.
\033[33m---------------------------------
\033[33m 1) WordListi başlat
\033[33m 2) Aracı yeniden başlat
\033[33m 3) Menüye Dön
\033[33m 4) Çık\033[0m
\033[33m---------------------------------
\033[0m""")
islemno = raw_input("\033[36mİşlem Numarası Giriniz:\033[0m ")

if(islemno == "1"):
	minimumkarekter = raw_input("Minimum Karekter Sayısını Giriniz: ")
	makskarekter = raw_input("Maximum Karekter Sayısını Giriniz: ")
	karekter = raw_input("Kullanılacak Karekterleri Belirleyiniz: ")
	kayityeri = raw_input("Kaydedilecek Yolu Belirtiniz: ")
	os.system("crunch " + minimumkarekter + " " + makskarekter + " " + karekter + " -o " + kayityeri)
	print("""
	\033[33m---------------------------------
	\033[33m 1) Aracı yeniden başlat
	\033[33m 2) Menüye dön
	\033[33m 3) Çık
	\033[33m---------------------------------\033[0m
	""")
	islemno = raw_input("\033[36mİşlem Numarası Giriniz:\033[0m ")
	if(islemno == "1"):
		os.system("sudo python ./tools/Wordlist_Oluşturma.py")
	
	elif(islemno == "2"):
		os.system("sudo python ./main.py")

	elif(islemno == "3"):
		os.system("clear")
		os.system("exit")
	else:
		os.system("sudo python ./tools/Wordlist_Oluşturma.py")
	
elif(islemno == "2"):
	os.system("sudo python ./tools/Wordlist_Oluşturma.py")
	
elif(islemno == "3"):
	os.system("sudo python ./main.py")

elif(islemno == "4"):
	os.system("clear")
	os.system("exit")
else:
	os.system("sudo python ./tools/Wordlist_Oluşturma.py")




