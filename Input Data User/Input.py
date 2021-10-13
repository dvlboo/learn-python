
# data selalu str
xumbra = input("input user = ")
print("xumbra = ",xumbra, ",type = ", type(xumbra))

#casting int
zumbra = int(input("scr number = "))
print("zumbra = ", zumbra, ",type = ", type(zumbra))

#casting float
kumbra = float(input("scr number = "))
print("zumbra = ", kumbra, ",type = ", type(kumbra))

#bool/biner akan menghasilkan nilai false jika data kosong
vumbra = bool(input("data = "))
print("vumbra = ", vumbra, ",type = ", type(vumbra))

#bool/biner akan menghasilkan nilai false jika data = 0
#akan menghasilkan true jika 
tumbra = bool(int(input("data = ")))
print("tumbra = ", tumbra, ",type = ", type(tumbra))