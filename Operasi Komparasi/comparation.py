# Operasi Komporasi => untuk membandingkan nilai

# setiap hasil dari operasi komporasi adalah boolean (True/False)

# >,<,>=,<=,==,!=,is,is not

# LEBIH DARI (>)
print("\n========== LEBIH DARI (>) \n")
a = 8
b = 4
c = 6
xy = a > 6
xz = b > 6
xa = c > 6
print("Nilai ",a, "> 6 = " ,xy)
print("Nilai ",b, "> 6 = " ,xz)
print("Nilai ",c, "> 6 = " ,xa)

# KURANG DARI (<)
print("\n========== KURANG DARI (<) \n")
a = 8
b = 4
c = 6
xy = a < 6
xz = b < 6
xa = c < 6
print("Nilai ",a, "< 6 = " ,xy)
print("Nilai ",b, "< 6 = " ,xz)
print("Nilai ",c, "< 6 = " ,xa)

# LEBIH DARI SAMA DENGAN (>=)
print("\n========== LEBIH DARI SAMA DENGAN (>=) \n")
a = 8
b = 4
c = 6
xy = a >= 6
xz = b >= 6
xa = c >= 6
print("Nilai ",a, ">= 6 = " ,xy)
print("Nilai ",b, ">= 6 = " ,xz)
print("Nilai ",c, ">= 6 = " ,xa)

# KURANG DARI SAMA DENGAN (<=)
print("\n========== KURANG DARI SAMA DENGAN (<=) \n")
a = 8
b = 4
c = 6
xy = a <= 6
xz = b <= 6
xa = c <= 6
print("Nilai ",a, "<= 6 = " ,xy)
print("Nilai ",b, "<= 6 = " ,xz)
print("Nilai ",c, "<= 6 = " ,xa)

# SAMA DENGAN (==)
print("\n========== SAMA DENGAN (==) \n")
a = 8
b = 4
c = 6
xy = a == 6
xz = b == 6
xa = c == 6
print("Nilai ",a, "== 6 = " ,xy)
print("Nilai ",b, "== 6 = " ,xz)
print("Nilai ",c, "== 6 = " ,xa)

# TIDAK SAMA DENGAN (!=)
print("\n========== TIDAK SAMA DENGAN (!=) \n")
a = 8
b = 4
c = 6
xy = a != 6
xz = b != 6
xa = c != 6
print("Nilai ",a, "!= 6 = " ,xy)
print("Nilai ",b, "!= 6 = " ,xz)
print("Nilai ",c, "!= 6 = " ,xa)


# 'is / is not' sebagai komparasi object identity
print("\n========== OBJECT IDENTITY (is) \n")
x = 5 # adalah assignment membuat object
y = 5
z = 6
hasil = x is y
xhasil = x is z

print("Nilai x =",x)
print("Nilai y =",y)
print("Nilai z =",z,"\n")

print("Nilai dari x is y =",hasil)
print("Nilai dari y is z =",xhasil)

print("\n========== OBJECT IDENTITY (is not) \n")

x = 7 # adalah assignment membuat object
y = 7
z = 12
hasil = x is not y
xhasil = x is not z

print("Nilai x =",x)
print("Nilai y =",y)
print("Nilai z =",z,"\n")

print("Nilai dari x is not y =",hasil)
print("Nilai dari y is not z =",xhasil)







