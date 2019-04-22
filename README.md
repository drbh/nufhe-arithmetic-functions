# Nufhe Arithmetic Functions

This repo contains functions that do binary addition using half adders, full adders and ripple addtion. The library expects to get each binary digit as an individual hidden variable. 


First we have to setup the keys for FHE
```
import nufhe

ctx = nufhe.Context()
secret_key, cloud_key = ctx.make_key_pair()
vm = ctx.make_virtual_machine(cloud_key)
```

Next we can break up a binary string 

```
a = '01000001' # 65
b = '01010100' # 84
# we expect 65 + 84 = 149 or 10010101

x = list(map(int,list(a)))
y = list(map(int,list(b)))
```

output
```
([1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 1, 0, 0])
```

Now pass this list to the adding function along with the vm that has the related cloud key

```
nuout = add_eight_bit_numbers(secret_key, vm, *x, *y)
nuout
```

output
```
[0, 1, 0, 0, 1, 0, 1, 0, 1]
```

if we concat the list together we get `010010101`

```
010010101 == 10010101 # expected value
```

Yay we have successfully added two binary numbers as completely hidden values! Checkout the [demo](./demo.py) script for some code to get started and look at the [functions](./funcs.py) to see how the `add_eight_bit_numbers` encrypts and runs the computation.