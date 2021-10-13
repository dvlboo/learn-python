# Nama : Kukuh Cokro Wibowo
# NIM : 210441100102

print("Operasi Temperature by Kuhhh\n")
print("---------------------------------")
print("\nSilahkan isi Nama kakak terlebih dahulu\n")
its_you = input("Nama Panggilan Kakak : ")
print("\nSelamat datang kak",its_you,"\n",
    "----------------------------------")

# Panduan
# Isi Suhu dengan angka (int), jangan ada tambahan apapun (str)

# Celcius
C = float(input("Masukkan Suhu Celcius Anda :"))
print("\nSuhu Celcius Kak",its_you,"saat ini adalah",C,"C")

# Pada Suhu Lain

R = (4/5)*C
print("Hasil ke Reamur     =",R,"R")

F = ((9/5)*C)+32
print("Hasil ke Fahrenheit =",F,"F")

K = C+273
print("Hasil ke Kelvin     =",K,"K")


# Konversi Reamur

print("\nSilahkan kak",its_you,"\n",
    "------------------------------")
R = float(input("Masukkan Suhu Reamur Anda :"))
print("\nSuhu Reamur kak",its_you,"saat ini adalah",R,"R")

# Pada Suhu Lain

C = (5/4)*R
print("Hasil ke Celcius    =",C,"C")

F = ((9/4)*R)+32
print("Hasil ke Fahrenheit =",F,"F")

K = ((5/4)*R)+273
print("Hasil ke Kelvin     =",K,"K")

# Konversi Fahrenheit

print("\nLagi kak",its_you,"\n",
    "---------------------------")
F = float(input("Masukkan Suhu Fahrenheit Anda :"))
print("\nSuhu Fahrenheit kak",its_you,"saat ini adalah",F,"F")

# Pada Suhu Lain

C = (5/9)*(F-32)
print("Hasil ke Celcius =",C,"C")

R = (4/9)*(F-32)
print("Hasil ke Reamur  =",R,"R")

K = (5/9)*(F-32)+273
print("Hasil ke Kelvin  =",K,"K")

# Konversi Kelvin

print("\nTerakhir kak",its_you,"\n",
    "------------------------------")
K = float(input("Masukkan Suhu Kelvin Anda :"))
print("\nSuhu Kelvin kak",its_you,"saat ini adalah",K,"K")

# Pada Suhu Lain

C = K-273
print("Hasil ke Celcius    =",C,"C")

R = (4/5)*(K-273)
print("Hasil ke Reamur     =",R,"R")

F = (9/5)*(K-273)+32
print("Hasil ke Fahrenheit =",F,"F")

print("\nTerimakasih telah mencoba kak",its_you,":)")


# GitHub : kzth4(Boo)