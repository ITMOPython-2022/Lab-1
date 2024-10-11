AXIS = f'\x1b[48;5;{1}m{" "}\x1b[0m'
GRAPH = f'\x1b[48;5;{2}m{" "}\x1b[0m'
print('    y')
for y in range(45 ,0 ,-3):
    if y < 10:
        space1 = ' '
    else:
        space1 = ''

    space2 = ' ' * (y // 3 - 1)
    print(y, space1, AXIS + space2 + GRAPH)
    
print(0, ' ', GRAPH + AXIS * 20, 'x')
print('   ', '0123456789...')