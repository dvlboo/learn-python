# not, or, xor

# NOT

print("- This is NOT Syntax\n" 
    "========NOT========") # Kebalikan
x = True
y = False
z = not x
z1 = not y
print('Nilai x =',x,"\n",
    "---------------------NOT","\n",
    "   Nilai Not x =",z,"\n\n",
    "Nilai Not y =",y, "\n",
    "---------------------NOT","\n"
    "   Nilai Not y =",z1,'\n')

# OR

print("- This is OR Syntax\n" 
    "========OR========") # Dominan(True)

p = False
q = False
r = p or q
print(p,"or",q,'=',r)
p = False
q = True
r = p or q
print(p,"or",q,' =',r)
p = True
q = False
r = p or q
print(p," or",q,'=',r)
p = True
q = True
r = p or q
print(p," or",q,' =',r)


