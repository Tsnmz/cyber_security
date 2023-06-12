#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.system("clear")
os.system("sudo apt-get install figlet")
os.system("clear")
print("\033[35m")
os.system("figlet Cyber Tools")
print("\033[0m")
print(""" 

\033[33m  Cyber Araçlarına Hoş Geldiniz.

\033[31m GitHub: \033[36mhttps://github.com/Tsnmz
\033[31m LinkedIn: \033[36mhttps://www.linkedin.com/in/tsnmz/
\033[31m GitHub: \033[36mhttps://github.com/Tsnmz/cyber_security\033[0m""")
print("\033[0m")
print("\033[32m---------------------------------------------")
print("""
\033[33m  1) Port Tarama
\033[33m  2) VPN Kontrol
\033[33m  3) Sunucu Zafiyet Analizi
\033[33m  4) Güvenlik Duvarı Tespiti
\033[33m  5) MAC Adres Değişikliği
\033[33m  6) Portlara Kaba Kuvvet Saldırısı
\033[33m  7) RootKit Taraması
\033[33m  8) Veri Tabanı Ele Geçirme
\033[33m  9) Wordlist Oluşturma
\033[33m 10) Zaafiyet Analizi
\033[33m 11) Wordpress Tarama
\033[33m 12) Çıkış
""")
print("\033[32m---------------------------------------------\033[0m")

islemno = raw_input("1-12 Arasında Bir Sayı Giririniz: ")


if(islemno == "1"):
	os.system("sudo python ./tools/Port_Tarama.py")
	
elif(islemno == "2"):
	os.system("sudo python ./tools/VPN_Kontrol.py")
	
elif(islemno == "3"):
	os.system("sudo python ./tools/Sunucu_Zafiyet_Aracı.py")	

elif(islemno == "4"):
	os.system("sudo python ./tools/Güvenlik_Duvarı_Tespiti.py")

elif(islemno == "5"):
	os.system("sudo python ./tools/MAC_Adres_Değiştirme.py")
	
elif(islemno == "6"):
	os.system("sudo python ./tools/Port_Kaba_Kuvvet.py")

elif(islemno == "7"):
	os.system("sudo python ./tools/RootKit_Taraması.py")

elif(islemno == "8"):
	os.system("sudo python ./tools/Veritabanı_Ele_Geçirme.py")

elif(islemno == "9"):
	os.system("sudo python ./tools/Wordlist_Oluşturma.py")

elif(islemno == "10"):
	os.system("sudo python ./tools/Zafiyet_Analizi.py")

elif(islemno == "11"):
	os.system("sudo python ./tools/Wordpress_Tarama.py")

elif(islemno == "12"):
	os.system("clear")
	os.system("exit")
else:
	os.system("sudo python ./main.py")



