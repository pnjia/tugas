#!/usr/bin/env python
# coding: utf-8

# In[16]:


#Operator aritmetika
num1= 10
num2 = 3

jumlah = num1 + num2
kurang = num1 - num2
kali = num1 * num2
bagi = num1 / num2
bagi_bulat = num1 // num2
pangkat = num1**num2
modulus = num1 % num2
print(jumlah)
print(kurang)
print(kali)
print(bagi)
print(modulus)


# In[15]:


#assignment Operator
x = 5
x += 10 # x = x + 10 => 15
print(x)
x -= 4 # x = x - 4 => 11
print(x)
x *= 2 # x = x * 2 => 22
print(x)
x /= 3  # x = x / 3 => 7....
print(x)
x //= 2 # x = x // 2 => 3.0
print(x)
x **= 3 # x = x ** 3 => 27
print(x)
x %= 2 # x = x % 2 => 1
print(x)

data = [1, 2, 3, 4, 5]
total = 0
for i in range(0, 5):
    total += data[i]
print("Total : ", total)    


# In[19]:


#Operator Perbandingan
bil1 = 8
bil2 = 7

is_equal = bil1 == bil2
is_not_equal = bil1 != bil2
is_great_than = bil1 > bil2
is_less_than = bil1 < bil2
is_greater_equal = bil1 >= bil2
is_less_equal = bil1 <= bil2
print(is_equal)
print(is_not_equal)
print(is_great_than)
print(is_less_than)
print(is_greater_equal)
print(is_less_equal)


# In[21]:


#Operator Logika
var1 = 4
var2 = 10

opr_and = var1 < var2 and var1 <=4 #True
opr_or = var1 >= var2 or var1 % 2 == 1 #False
opr_not = not opr_or #True

print(opr_and)
print(opr_or)
print(opr_not)


# In[31]:


#Operator Identitas
fruits = ["Apple", "Mangoes", "Watermelon"]
my_favorite_fruits = fruits #lokasi memori yang sama
your_fruits = ["Apple", "Mangoes", "Watermelon"] #lokasi memori yang berbeda

print(fruits is my_favorite_fruits)
print(fruits is your_fruits)
print(fruits is not my_favorite_fruits)
print(fruits is not your_fruits)

a = 5
b = 5 #python menggunakan metode hashing dalam memberikan nilai variabel
print(a is b)
print(a is not b)


# In[36]:


#Operator Keanggotaan
student_names = ["Andi", "Beni", "Chika"]
print("Beni" in student_names)
print("Andi" not in student_names)
print("Defi" in student_names)
print("Defi" not in student_names)


# In[40]:


#Operator Bitwise & (and), |(or), ^(xor)
nilai_and = 255 & 15
nilai_or = 255 | 15
nilai_xor = 255 ^ 15
#11111111 (255)
#00001111 (15)
#-------- and
#00001111 => 15
#-------- or
#11111111 => 255
#-----=-- xor
#11110000 => 240
print(nilai_and)
print(nilai_or)
print(nilai_xor)

