spot1=f'\x1b[48;5;{1}m{" "}\x1b[0m'
spot2=f'\x1b[48;5;{2}m{" "}\x1b[0m'
print('    y')
space=2
for y in range(45,0,-3):
    print(y,' '*(space-len(str(y))),spot1+' '*(y//3-1)+spot2)
print(0,' ',spot2+spot1*20,'x')
print('   ','0123456789...')