from funcs import *

a = '01000001'
b = '01010100'

x = list(map(int,list(a)))
y = list(map(int,list(b)))

c = bin(int(a,2) + int(b,2))

out = list(map(int,list(c[2:])))

print("PYTHON OUTPUT: ", out)

nuout = add_eight_bit_numbers(secret_key, vm, *x, *y)

print("NUFHE OUTPUT: ", nuout)
