def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
    print('blastoff(发射)!')


import dis

# dis.dis(countdown)

c = countdown.__code__.co_code
import opcode

print(opcode.opname[c[0]])

print(opcode.opname[c[3]])
