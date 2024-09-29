a=[float(x) for x in open('sequence.txt')]
q=w=0
spot1=f'\x1b[48;5;{1}m{"   "}\x1b[0m'
spot2=f'\x1b[48;5;{2}m{"   "}\x1b[0m'
for x in a:
    if x<=0:
        if x>-5:q+=1
        if x<-5:w+=1
for i in range(max(q,w),0,-1):
    if i<=q and i<=w:print(spot1,spot2)
    if i<=q and i>w:print(spot1)
    if i>q and i<=w:print('   ', spot2)
print('>-5','<-5')