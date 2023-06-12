#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("clear")
os.system("figlet MAC Degistirme")
print("""
MAC Adres Değiştirme Programına Hoş Geldiniz
\033[33m---------------------------------
\033[33m 1) MAC Adresi Rastgele Olarak Belirle
\033[33m 2) MAC Adresi Manuel Olarak Belirle
\033[33m 3) MAC Adresi Orjinale Döndür
\033[33m 4) MAC Adresi Değiştirilecek Aygıtları Listele
\033[33m 5) Menüye Dön
\033[33m 6) Çık
\033[33m---------------------------------
\033[0m """)

islemno = raw_input("\033[32m 1-6 arasında sayı girerek lütfen bir işlem seçiniz:\033[0m  ")
print(" ")
if(islemno == "1"):
	os.system("sudo ifconfig")
	print(""" """)
	aygit = raw_input("MAC adresi değiştilecek aygıtı belirleyiniz: ")
	
	os.system("sudo macchanger -r " + aygit) 
	
	print(""" """)
	print("\033[92mYeni MAC Adresi Rastgele Olarak Belirlendi.")
	
elif(islemno == "2"):
	os.system("sudo ifconfig")
	print(""" """)
	aygit = raw_input("MAC adresi değiştilecek aygıtı belirleyiniz: ")
	macadres = raw_input("Yeni MAC Adresinizi Giriniz: ")
	os.system("sudo macchanger --mac " + macadres + " " + aygit) 
	print(""" """)
	print("\033[92mYeni MAC Adresi Manuel Olarak Belirlendi.")
	
elif(islemno == "3"):
	os.system("sudo ifconfig")
	print(""" """)
	aygit = raw_input("MAC adresi değiştilecek aygıtı belirleyiniz: ")
	os.system("sudo macchanger -p " + aygit) 
	print(""" """)
	print("\033[92mMAC Adresiniz Ojinal Adrese Dönüştürülmüştür.")
	
elif(islemno == "4"):
	os.system("sudo ifconfig")
	print(""" """)
	print("\033[92mAktif Aygıtlar Listelenmiştir")
	
elif(islemno == "5"):
	os.system("sudo python ./main.py")
	

elif(islemno == "6"):
	os.system("clear")
	os.system("exit")

else:
	os.system("sudo python ./tools/MAC_Adres_Değiştirme.py")
	
print("""
\033[33m---------------------------------
\033[33m 1) Aracı yeniden başlat
\033[33m 2) Menüye Dön
\033[33m 3) Çık\033[0m
\033[33m---------------------------------
""")

islemno = raw_input("\033[32mLütfen bir değer giriniz:\033[0m ")
if(islemno == "1"):
	os.system("sudo python ./tools/MAC_Adres_Değiştirme.py")
	
elif(islemno == "2"):
	os.system("sudo python ./main.py")

elif(islemno == "3"):
	os.system("clear")
	os.system("exit")
else:
	os.system("sudo python ./tools/MAC_Adres_Değiştirme.py")
	
	
	
	
