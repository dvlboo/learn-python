# operasi bitwise / biner/ binary


print("Menentukan Operasi Bitwise")
a = int(input("Masukkan Nilai a : "))
b = int(input("Masukkan Nilai b : "))

# bitwise OR (|)
c = a | b
print('\n===============OR==============')
print('nilai :',a,"binary   :",format(a,'08b'))
print('nilai :',b,"binary   :",format(b,'08b'))
print("-------------------------------(|)")
print('nilai :',c,"binary   :",format(c,'08b'))

# bitwise AND (&)
c = a & b
print('\n==============AND==============')
print('nilai :',a,"binary   :",format(a,'08b'))
print('nilai :',b,"binary   :",format(b,'08b'))
print("-------------------------------(&)")
print('nilai :',c,"binary   :",format(c,'08b'))

# bitwise XOR (^)
c = a ^ b
print('\n==============XOR==============')
print('nilai :',a,"binary   :",format(a,'08b'))
print('nilai :',b,"binary   :",format(b,'08b'))
print("-------------------------------(^)")
print('nilai :',c,"binary   :",format(c,'08b'))

# bitwise NOT (~)
c = ~a
d = ~b
print('\n==============NOT==============')
print('nilai :',a,"binary   :",format(a,'08b'))
print('nilai :',b,"binary   :",format(b,'08b'))
print("-------------------------------(~)")
print('nilai :',c,"binary   :",format(c,'08b'))
print('nilai :',d,"binary   :",format(d,'08b'))
print("-------------------------------(^)")
print('nilai :',d^c,"binary   :",format(d^c,'08b'))

# shifting

#shift Right (>>)
print(30*"+")
print("\n=====Shifting Bitwise=====")
z = int(input("Geser Kanan Nilai a : "))
c = a >> z
print('\n===========Shift Right===========')
print('nilai :',a,"binary   :",format(a,'08b'))
print("-------------------------------(>>",z,")")
print('nilai :',c,"binary   :",format(c,'08b'))

#shift Left (<<)
print("\n")
v = int(input("Geser Kiri Nilai b : "))
d = b << v
print('\n==============Shift Left==============')
print('nilai :',a,"binary   :",format(a,'08b'))
print("-------------------------------(<<",v,")")
print('nilai :',d,"binary   :",format(d,'08b'))
