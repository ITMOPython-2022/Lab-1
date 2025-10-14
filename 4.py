with open("sequence.txt") as sequence:
    data = [float(line) for line in sequence]
    
less_than = 0
greater_than = 0

spot1 = f'\x1b[48;5;{1}m{"   "}\x1b[0m'
spot2 = f'\x1b[48;5;{2}m{"   "}\x1b[0m'

for num in data:
    if num <= 0:
        if num > -5:
            less_than += 1
        elif num < -5:
            greater_than += 1

for amount in range(max(less_than, greater_than), 0, -1):
    if amount <= less_than and amount <= greater_than :
        print(spot1, spot2)
    elif amount <= less_than and amount > greater_than:
        print(spot1)
    elif amount > less_than and amount <= greater_than:
        print('   ', spot2)
print('>-5', '<-5')