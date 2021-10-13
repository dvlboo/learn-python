# Latihan Komparasi dan Boolean

print("Latihan Komparasi dan Boolean by Boo")
print(40*"=","\n")

#Lat 1 
print("Tentukan Nilai dari +++++5-----10+++++\n")
UserPoint = int(input("Masukkan angka < 5 atau angka > 10\n:"))

# +++++5-----
isUser_KurangDari = UserPoint < 5
print("\nPada +++++5-----\nNilai dari",UserPoint,"adalah",isUser_KurangDari)

# -----10+++++
isUser_LebihDari = UserPoint > 10
print("Pada -----10+++++\nNilai dari",UserPoint,"adalah",isUser_LebihDari)
# Hasil
UserCorrect = isUser_KurangDari or isUser_LebihDari
print("\nMaka Nilai sebenarnya dari",UserPoint,"\nMenurut +++++5-----10+++++ adalah",UserCorrect)

print(40*"=","\n")

#Lat 2
print("Tentukan Nilai dari -----5+++++10-----\n")
UserPoint_two = int(input("Masukkan angka > 5 dan angka < 10\n:"))
# -----5+++++
isUser_LebihDariTwo = UserPoint_two > 5
print("\nPada -----5+++++\nNilai dari",UserPoint_two,"adalah",isUser_LebihDariTwo)

# +++++10-----
isUser_KurangDariTwo = UserPoint_two < 10
print("Pada +++++10-----\nNilai dari",UserPoint_two,"adalah",isUser_KurangDariTwo)
# Hasil
UserCorrectTwo = isUser_LebihDariTwo and isUser_KurangDariTwo
print("\nMaka Nilai sebenarnya dari",UserPoint_two,"\nMenurut -----5+++++10----- adalah",UserCorrectTwo)