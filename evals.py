def req(i):
    return i*5

def feq(i):
    return i*4
stat=input('enter func\n')
for i in range(1,5):
    if stat=="req(i)":
        print(eval(stat))
    elif stat=="feq(i)":
        print(eval(stat))
    else:
        print('error')