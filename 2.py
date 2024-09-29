startgap=gap=10
f=0
spot=f'\x1b[48;5;{1}m{" "}\x1b[0m'
for i in range(11):
    space=(startgap-gap)*2
    if gap==0:f=1
    st=' '*gap+spot+' '*space+spot+' '*gap
    print(st*4)
    if f!=1:gap-=2
    if f==1:gap+=2
