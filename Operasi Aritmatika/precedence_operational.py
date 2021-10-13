# Operasi Prioritas
'''
    1. ()
    2. EXPONEN "**"
    3. PERKALIAN DLL "*,/,%,**,//"
    4. PENJUMLAHAN DAN PENGURANGAN "+,-"
'''
a = 7
b = 4
c = 9
d =15

zx = a + d * b - c ** b // b * d / c % b
print(a,'+',d,'x',b,'-',c,'^',b,'//',b,'x',d,'/',c,'%',b,'=', zx)

zx = (a + d) * (b - c) ** b // b * d / c % b
print('(',a,'+',d,')x(',b,'-',c,' )^',b,'//',b,'x',d,'/',c,'%',b,'=', zx)