circwidth=lenred=6
k=2
lenrow=56
row=14
for r in range(1,row+1):
    if 4<r<=row-2 and lenred>=circwidth:
        lenwhite=(lenrow-lenred)//2
        white=f'\x1b[48;5;{7}m{" "*lenwhite}\x1b[0m'
        red=f'\x1b[48;5;{1}m{" "*lenred}\x1b[0m'
        print(white+red+white)
        if lenred==14:
            k-=1
        if k==0:
            lenred-=4
        if lenred<circwidth*2 and k!=0:
            lenred+=4
    else:print(f'\x1b[48;5;{7}m{" "*lenrow}\x1b[0m')