#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Input & Output
bil1 = int(input("Isikan bilangan 1: "))
bil2 = int(input("Isikan bilangan 2: "))

hasil = bil1 + bil2

print("Hasil penjumlahan", bil1, "+", bil2, "=",hasil)


# In[6]:


#program menghitung luas dan keliling persegi panjang

panjang = input("Masukkan nilai panjang : ") 
lebar = input("Masukkan nilai lebar : ")

luas = int(panjang) * int(lebar)
keliling = 2 * (int(panjang) + int(lebar))

print("Luas : ", luas)
print("Keliling : ", keliling)


# In[10]:


print("A", "B", "C", "D", sep="|") #sep = seperator / pembatas


# In[11]:


print("A", "B", "C", "D", sep="\n")


# In[12]:


print("A", "B", "C", "D", sep="\n", end="^_^")


# In[ ]:


num_1 = 8
num_2 = 10

# Hasil dari 8 modulus 10 = 8

print("Hasil dari {} modulus {} =  {}".format(num_1, num_2, num_1%num_2))


# In[15]:


#Memformat dengan key (kunci)

fname = "Rudi"
mname = "Hartono"
lname = "Darmawan"

print("Nama anda {1} {0} {2}".format(fname, mname, lname))


# In[17]:


print('Nama anda {nama}, nilai anda {nilai}'.format(nama="Andi", nilai=70))


# In[26]:


univ = "Universitas Nusa Putra"

print("Karakter pertama : ", univ[0])
print("Karakter terakhir : ", univ[-1])
#Universitas
print(univ[0:11])
print(univ[-5:])
print(univ[17:])


# In[30]:


f_name = "Rudi"
l_name = "Andri"

print(f'Nama saya {f_name} {l_name}')


# In[31]:


first = 100
second = 20

print(f'Hasil penjumlahan {first} + {second} = {first + second}')


# In[4]:


#Fungsi string

#Split --> memisahkan string berdasarkan karakter tertentu
nama = "Andri,Budi,Cika"
nama2 = "Andri Budi Cika"

print(nama2.split())
print(nama.split(","))

#join --> mennggabungkan string ke dalam kumpulan karakter
print('@'.join(nama.split(',')))

#input tanggal lahir --> 18/Oktober/2010
#input nama --> bill Gate
#output :
#Tanggal : 18, bulan:Oktober, Tahun :2010
#Nama Inisial : BG

tgl = input("Masukkan tanggal lahir : ")
nama = input("Masukkan nama : ")
pemisah = tgl.split("/")
print(f"Tanggal : {pemisah[0]}, bulan:{pemisah[1]}, Tahun:{pemisah[2]}")
pemisah2 = nama.split()
nama_pertama = pemisah2[0]
nama_terakhir = pemisah2[1]
print(f"Nama inisial : {nama_pertama[0]+nama_terakhir[0]}")

