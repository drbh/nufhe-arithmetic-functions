import nufhe
import sys

def half_adder(vm, cipherbit1, cipherbit2):
    sha = vm.gate_xor(cipherbit1, cipherbit2)
    cha = vm.gate_and(cipherbit1, cipherbit2)
    return sha, cha

def full_adder(vm, P, Q, C):
    s, co = half_adder(vm, P, Q)
    s2, co2 = half_adder(vm, s, C)
    carry = vm.gate_xor(co, co2)
    return carry, s2

def eight_bit_adder(vm, 
    a1, a2, a3, a4, a5, a6, a7, a8, 
    b1, b2, b3, b4, b5, b6, b7, b8, ecarry):

    co1, sm1 = full_adder(vm, a8, b8, ecarry ) 
    co2, sm2 = full_adder(vm, a7, b7, co1)
    co3, sm3 = full_adder(vm, a6, b6, co2)
    co4, sm4 = full_adder(vm, a5, b5, co3)
    co5, sm5 = full_adder(vm, a4, b4, co4)
    co6, sm6 = full_adder(vm, a3, b3, co5)
    co7, sm7 = full_adder(vm, a2, b2, co6)
    co8, sm8 = full_adder(vm, a1, b1, co7)
    return co8, sm8, sm7, sm6, sm5, sm4, sm3, sm2, sm1

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def add_eight_bit_numbers(secret_key, vm,
    a1, a2, a3, a4, a5, a6, a7, a8,
    b1, b2, b3, b4, b5, b6, b7, b8):

    cipher_a1 = ctx.encrypt(secret_key, [a1])
    cipher_a2 = ctx.encrypt(secret_key, [a2])
    cipher_a3 = ctx.encrypt(secret_key, [a3])
    cipher_a4 = ctx.encrypt(secret_key, [a4])
    cipher_a5 = ctx.encrypt(secret_key, [a5])
    cipher_a6 = ctx.encrypt(secret_key, [a6])
    cipher_a7 = ctx.encrypt(secret_key, [a7])
    cipher_a8 = ctx.encrypt(secret_key, [a8])

    cipher_b1 = ctx.encrypt(secret_key, [b1])
    cipher_b2 = ctx.encrypt(secret_key, [b2])
    cipher_b3 = ctx.encrypt(secret_key, [b3])
    cipher_b4 = ctx.encrypt(secret_key, [b4])
    cipher_b5 = ctx.encrypt(secret_key, [b5])
    cipher_b6 = ctx.encrypt(secret_key, [b6])
    cipher_b7 = ctx.encrypt(secret_key, [b7])
    cipher_b8 = ctx.encrypt(secret_key, [b8])
    
    ecarry = ctx.encrypt(secret_key, [0]) 
    
    print(sizeof_fmt(sys.getsizeof(cipher_a2.dumps())*16))

    co8, sm8, sm7, sm6, sm5, sm4, sm3, sm2, sm1 = eight_bit_adder(vm, 
        
        cipher_a1, cipher_a2, cipher_a3, cipher_a4, 
        cipher_a5, cipher_a6, cipher_a7, cipher_a8, 

        cipher_b1, cipher_b2, cipher_b3, cipher_b4, 
        cipher_b5, cipher_b6, cipher_b7, cipher_b8,
                                                                 
        ecarry)

    dco8 = ctx.decrypt(secret_key, co8)
    dsm8 = ctx.decrypt(secret_key, sm8)
    dsm7 = ctx.decrypt(secret_key, sm7)
    dsm6 = ctx.decrypt(secret_key, sm6)
    dsm5 = ctx.decrypt(secret_key, sm5)
    dsm4 = ctx.decrypt(secret_key, sm4)
    dsm3 = ctx.decrypt(secret_key, sm3)
    dsm2 = ctx.decrypt(secret_key, sm2)
    dsm1 = ctx.decrypt(secret_key, sm1)


    return list(map(int,
        [*dco8, *dsm8, *dsm7, *dsm6, *dsm5, *dsm4, *dsm3, *dsm2, *dsm1] ))
