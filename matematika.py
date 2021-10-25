from treeviz.treeviz import Node
from os import system
from time import sleep
from math import *
from fractions import Fraction as Fr
from statistics import mean,median,mode
#|
#|
#|
def penjumlahan():
	x = Fr(input('😸 angka 1 : '))
	y = Fr(input('😁 angka 2 : '))
	total = x+y
	print (f'{x} + {y} = {total}')

def pengurangan():
	x = Fr(input('😸 angka 1 : '))
	y = Fr(input('😁 angka 2 : '))
	total = x-y
	print (f'{x} - {y} = {total}')

def perkalian():
	x = Fr(input('😸 angka 1 : '))
	y = Fr(input('😁 angka 2 : '))
	total = x*y
	print (f'{x} x {y} = {total}')

def pembagian():
	x = Fr(input('😸 angka 1 : '))
	y = Fr(input('😁 angka 2 : '))
	total = x/y
	print (f'{x} / {y} = {total}')

def faktorial():
	x = Fr(input("😌 masukkan angka: "))
	total = factorial(x)
	print (f'{x}! = {total}')

def eksponenaial():
	x = Fr(input('😸 masukkan angka: '))
	y = Fr(input('😁 masukkan pangkat: '))
	total = (x**y)
	print (f'{x} ^ {y} = {total}')

# data
# done

def means():
	x = input('masukkan data: ')
	data = []
	for i in x.split(","):
		data.append(int(i))
	print (f'\ndata setelah diurutkan = {sorted(data)}')
	print (f'mean = {mean(data)}')

def medians():
	x = input('masukkan data: ')
	data = []
	for i in x.split(","):
		data.append(int(i))
	print (f'\ndata setelah diurutkan = {sorted(data)}')
	print (f'median = {median(data)}')

def moduss():
	x = input('masukkan data: ')
	data = []
	for i in x.split(","):
		data.append(int(i))
	print (f'\ndata setelah diurutkan = {sorted(data)}')
	print (f'modus = {mode(data)}')


def pengakaran():
	x = Fr(input('🌚 masukkan angka: '))
	total = sqrt(x)
	print (f'√({x}) = {total}')

def menu():
	system("clear")
	print ("\033[34;1m\033[47;1mScript matematika\033[0m\033[32;1m");print ("")
	print ("\x1b[34;1m\033[47;0mauthor: Ahmad")
	print ('facebook: -')
	print ('whatsapp: 085342600951\033[0m\033[32;1m\n')
	menu = Node("MENU")
	kalkulator = Node("1.\033[36;1mkalkukator\033[32;1m")
	#turunan kalkukator
	penjumlahan1 = Node("1a) Penjumlahan")
	pengurangan1 = Node("1b) Pengurangan")
	perkalian1 = Node("1c) Perkalian")
	pembagian1 = Node("1d) Pembagian")
	statistik1 = Node("\033[36;1m2.Statistik\033[32;1m")
	#turunan statistik
	mean1 = Node("2a) Mean")
	median1 = Node("2b) Median")
	modus1 = Node("2c) Modus")
	tambahan1 = Node('\033[36;1m3.Tambahan\033[32;1m')
	#turunan tambahan
	faktorial1 = Node("3a) Faktorial")
	eksponensial1 = Node("3b) Eksponen")
	akar1 = Node("3c) Pengakaran")
	#play
	#utama
	menu.add_child(kalkulator)
	menu.add_child(statistik1)
	menu.add_child(tambahan1)
	#kalkulator
	kalkulator.add_child(penjumlahan1)
	kalkulator.add_child(pengurangan1)
	kalkulator.add_child(perkalian1)
	kalkulator.add_child(pembagian1)
	#statistik
	statistik1.add_child(mean1)
	statistik1.add_child(median1)
	statistik1.add_child(modus1)
	#tambahan
	tambahan1.add_child(faktorial1)
	tambahan1.add_child(eksponensial1)
	tambahan1.add_child(akar1)
	#munculkan
	menu.visualize(line_space=0)
	#menginput pilihan
	pilihan = input('\n\033[33;1mpilihan >> ')
	#boolean
	if pilihan == "1":
		system("clear")
		print ("\n1.penjumlahan")
		print ("2.pengurangan")
		print ("3.pembagian")
		print ("4.perkalian")
		#boolean2
		print ("");pilihan_2 = input('pilihan >> ')
		if pilihan_2 == "1":
			print ('')
			penjumlahan()
		elif pilihan_2 == "2":
			print ("")
			pengurangan()
		elif pilihan_2 == "3":
			print ("")
			perkalian()
		elif pilihan_2 == "4":
			print ("")
			pembagian()
		else: print ('\n\033[31;1mkesalahan input\n\033[0m')
	elif pilihan == "2":
		system("clear")
		print ('1 mean')
		print ('2.median')
		print ('3.modus')
		#boelan3
		print ("");pilihan_3 = input('pilihan >> ')
		if pilihan_3 == "1":
			print ("")
			means()
		elif pilihan_3 == "2":
			print ("")
			medians()
		elif pilihan_3 == "3":
			print ("")
			moduss()
		else: print ('\n\033[31;1mkesalahan input\n\033[0m')
	elif pilihan == "3":
		system("clear")
		print ('1.faktorial')
		print ('2.eksponensial')
		print ('3.pengakaran')
		#boelan4
		print ("");pilihan_4 = input('pilihan >> ')
		if pilihan_4 == "1":
			print ('')
			faktorial()
		elif pilihan_4 == '2':
			print ("")
			eksponensial()
		elif pilihan_4 == '3':
			print ("")
			pengakaran()
		else: print ('\n\033[31;1mkesalahan input\n\033[0m')
	elif pilihan == '1a':
		print ("")
		penjumlahan()
	elif pilihan == '1b':
		print ("")
		pengurangan()
	elif pilihan == '1c':
		print ("")
		perkalian()
	elif pilihan == '1d':
		print ("")
		pembagian()
	elif pilihan == '2a':
		print ("")
		means()
	elif pilihan == '2b':
		print ("")
		medians()
	elif pilihan == '2c':
		print ("")
		moduss()
	elif pilihan == '3a':
		print ("")
		faktorial()
	elif pilihan == '3b':
		eksponensial()
	elif pilihan == '3c':
		print ('')
		pengakaran()
	else: print ('\n\033[31;1mkesalahan input\n\033[0m')
menu()

