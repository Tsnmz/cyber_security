#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.system("clear")

os.system("figlet Zafiyet Analizi")


print("""\033[36mZafiyet Analizi Aracına Hoş Geldiniz 
\033[33m---------------------------------
\033[33m 1) Zafiyet Analizini Başlat
\033[33m 2) Aracı yeniden başlat
\033[33m 3) Menüye Dön
\033[33m 4) Çık\033[0m
\033[33m---------------------------------
\033[0m

\033[31mNot:\033[0m Bu araç bulunduğunuz işletim sisteminin zafiyet analizini yapar.
""")

islemno = raw_input("\033[36mİşlem Numarası Giriniz:\033[0m ")

 
if(islemno == "1"):
	os.system("lynis audit system")
	print("""
	\033[33m---------------------------------
	\033[33m 1) Aracı yeniden başlat
	\033[33m 2) Menüye dön
	\033[33m 3) Çık
	\033[33m---------------------------------\033[0m
	""")
	islemno = raw_input("\033[36mİşlem Numarası Giriniz:\033[0m ")
	if(islemno == "1"):
		os.system("sudo python ./tools/Zafiyet_Analizi.py")
	
	elif(islemno == "2"):
		os.system("sudo python ./main.py")

	elif(islemno == "3"):
		os.system("clear")
		os.system("exit")
	else:
		os.system("sudo python ./tools/Zafiyet_Analizi.py")
	
elif(islemno == "2"):
	os.system("sudo python ./tools/Zafiyet_Analizi.py")
	
elif(islemno == "3"):
	os.system("sudo python ./main.py")

elif(islemno == "4"):
	os.system("clear")
	os.system("exit")
else:
	os.system("sudo python ./tools/Zafiyet_Analizi.py")
