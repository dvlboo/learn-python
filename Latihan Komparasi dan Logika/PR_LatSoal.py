# PR Soal Komparasi dan Boolean

print("Soal No 1\n"
    "-----0+++++5-----8+++++11-----")
print("Soal No 2\n"
    "+++++0-----5+++++8-----11+++++")

print("Jawab :\n")

print("Number 1")
UserPoint = int(input("Masukkan angka > 0 atau angka < 5\n"
    "dan angka > 8 atau angka < 11\n:"))

# -----0+++++
isUser_LebihDariNol = UserPoint > 0
print("\nPada  -----0+++++\nNilai dari",UserPoint,"adalah",isUser_LebihDariNol)

# +++++5-----
isUser_KurangDariLima = UserPoint < 5
print("Pada +++++5-----\nNilai dari",UserPoint,"adalah",isUser_KurangDariLima)

# -----8+++++
isUser_LebihDariDelapan = UserPoint > 8
print("Pada -----8+++++\nNilai dari",UserPoint,"adalah",isUser_LebihDariDelapan)

# +++++11-----
isUser_KurangDariSebelas = UserPoint < 11
print("Pada +++++11-----\nNilai dari",UserPoint,"adalah",isUser_KurangDariSebelas)

# Hasil
UserCorrect = ((isUser_LebihDariNol and isUser_KurangDariLima) or 
    (isUser_LebihDariDelapan and isUser_KurangDariSebelas))
print("\nMaka Nilai sebenarnya dari",UserPoint,"\n"
    "Menurut -----0+++++5-----8+++++11-----\n"
    "Adalah",UserCorrect)

print("\n",40*"=")
print("\nNumber 2")
UserPointTwo = int(input("Masukkan angka < 0 atau angka > 5\n"
    "dan angka < 8 atau angka > 11\n:"))

# +++++0-----
isUser_KurangDariNol = UserPointTwo < 0
print("\nPada  +++++0-----\nNilai dari",UserPointTwo,"adalah",isUser_KurangDariNol)

# -----5+++++
isUser_LebihDariLima = UserPointTwo > 5
print("Pada -----5+++++\nNilai dari",UserPointTwo,"adalah",isUser_LebihDariLima)

# +++++8-----
isUser_KurangDariDelapan = UserPointTwo < 8
print("Pada +++++8-----\nNilai dari",UserPointTwo,"adalah",isUser_KurangDariDelapan)

# -----11+++++
isUser_LebihDariSebelas = UserPointTwo > 11
print("Pada -----11+++++\nNilai dari",UserPointTwo,"adalah",isUser_LebihDariSebelas)

# Hasil
UserCorrectTwo = ((isUser_KurangDariNol or isUser_LebihDariLima) and 
    (isUser_KurangDariDelapan or isUser_LebihDariSebelas))
print("\nMaka Nilai sebenarnya dari",UserPointTwo,"\n"
    "Menurut -----0+++++5-----8+++++11-----\n"
    "Adalah",UserCorrectTwo)
