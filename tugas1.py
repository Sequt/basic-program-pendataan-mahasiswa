import os
import sys

class Mahasiswa:
        nim=''
        nama=''
nilai=''

pilih = 0
dataSiswa = []

def menu():
	os.system('cls')
	print("---Program pendataan Mahasiswa---");
	print("-------------------------------------------")
	print("1. Input Data Mahasiswa")
	print("2. Tampilkan Data Mahasiswa")
	print("3. Cari Nilai Mahasiswa Tertinggi")
	print("4. Cari Nilai Mahasiswa Terendah")
	print("5. Author")
	print("6. Keluar Aplikasi")
	pilih = int(input("Masukkan pilihan anda : "))
	if pilih == 1 :
		pilih1()
		menu()
	elif pilih == 2:
		tampil()
		input("kembali menu utama")
		menu()
	elif pilih == 3:
		index_update=-1
		tampil()
		input("kembali menu utama") 
		menu()
	elif pilih ==4:
		os.system('cls') 
		tampil()
		input("kembali menu utama") 
		menu()
	elif pilih == 5 :
		author()
		input("\n\n kembali menu utama") 
		menu()
	elif pilih == 6 :
		sys.exit()

def tampil():
	os.system('cls');
	print("DATA MAHASISWA")
	for data in dataSiswa:
		print("Nim : "+str(data.nim)) 
		print("Nama : "+data.nama) 
		print("Nilai : "+str(data.nilai))
		print("----------------------")
		
def author():
	os.system('cls')
	

def pilih1():
	ulang = 'Y'
	while ulang in('y', 'Y'):
		os.system('cls')
		siswaBaru = Mahasiswa() 
		print("INPUT DATA MAHASISWA ") 
		siswaBaru.nim = (int(input("masukkan nim  Mahasiswa: "))) 
		siswaBaru.nama = (input("masukkan nama Mahasiswa : ")) 
		siswaBaru.nilai = (int(input("masukkan nilai Mahasiswa : ")))
		dataSiswa.append(siswaBaru) 
		ulang = input("Apakah Anda Ingin Mengulang (Y/ T)? ")		

menu()
