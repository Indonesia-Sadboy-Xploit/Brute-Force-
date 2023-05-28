import os
import sys
import time


os.system("clear")
print("\033[32;1m ")
os.system("figlet BruteForce")
print("|=================|")
print("Name Author: Smile")
print("|=================|")
print("1)BruteForce Guess")
print("2)BruteForce Crack Facebook Wordlist")
print("3)BruteForce Crack Check Wordlist Web Wordprees Keyword")
print("4)info tools")
print("5)Exit")
print("=====================")
select = input("Please Select:")
if select =="1":
	print("wait...")
	print("Ctrl + C From Exit")
	time.sleep(5)
	write = input("Please Write From Guess:")
	for x in range(1000000000000):
		write = input("Please Write From Guess:")
elif select =="2":
	os.system("clear")
	print("=======================")
	print("NOTE: only applies to passwords that are translucent 123456 and so on")
	print("=======================")
	email = input("name:")
	print("wait....")
	time.sleep(5)
	PythonBf = open("wl1.txt", "r").readlines()
	for line in PythonBf:
		password = line.strip()
	print("password check:", email+password)
	print("wait 3 seconds")
	time.sleep(3)
	PythonBf = open("wl2.txt", "r").readlines()
	for line in PythonBf:
		password = line.strip()
		print("password check:", email+password)
		print("wait 3 seconds")
		time.sleep(3)
		PythonBf = open("wl3.txt", "r").readlines()
	for line in PythonBf:
		password = line.strip()
		print("password check:", email+password)
		print ("wait 3 seconds")
		time.sleep(3)
		PythonBf = open("wl4.txt", "r").readlines()
	for line in PythonBf:
		password = line.strip()
		print("password check:", email+password)
		print ("wait 3 seconds")
		time.sleep(3)
		PythonBf = open("wl5.txt", "r").readlines()
	for line in PythonBf:
		password = line.strip()
		print("password check:", email+password)
		print ("wait 3 seconds")
		time.sleep(3)
		PythonBf = open("wl6.txt", "r").readlines()
	for line in PythonBf:
		password = line.strip()
		print("password check:", email+password)
		print ("wait 3 seconds")
		time.sleep(3)
		PythonBf = open("wl7.txt", "r").readlines()
	for line in PythonBf:
		password = line.strip()
		print("password check:", email+password)
		print ("wait 3 seconds")
		time.sleep(3)
		PythonBf = open("wl8.txt", "r").readlines()
	for line in PythonBf:
		password = line.strip()
		print("password check:", email+password)
		print ("wait 3 seconds")
		time.sleep(3)
		PythonBf = open("wl9.txt", "r").readlines()
	for line in PythonBf:
		password = line.strip()
		print("password check:", email+password)
		print("===================}")
		print("Check This Password!")
		print("{===================")
elif select =="3":
		os.system("clear")
		print("=====================")
		print("NOTE: Only Applies To WordPress Vulnerable To This Keyword Good Luck!")
		print("=====================")
		PythonBf = open("wl-wordpress.txt", "r").readlines()
		for line in PythonBf:
			Keyword = line.strip()
			time.sleep(3)
			print("Check Keyword!:", Keyword)
elif select =="4":
			print("|=========================================================|")
			print("This tool aims to crack a password using the bruteforce method. Bruteforce is a brutal attack, namely an attack technique against a computer security system that uses trials of all keys.")
			print("|=========================================================|")	
elif select =="5":
	print("==========")
	print("GOOD BYE!")
	print("==========")
	sys.exit(3)

			
			
		
		
		
		
	
	
	
		
	
