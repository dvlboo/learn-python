a_int = 10
print("data = ", a_int, "Type = ", type(a_int))

b_float = float(a_int)
print("data = ", b_float, "Type = ", type(b_float))

c_str = str(a_int)
print("from int data = ", c_str, "Type = ", type(c_str))

c_str2 = str(b_float)
print("from float data = ", c_str2, "Type = ", type(c_str2))

d_bool = bool(c_str)
print("data = ", d_bool, "Type = ", type(d_bool))
