n1=0
n2=1
number=int(input('enter the fibonic number'))
for i in range(1, number+1):
    n3=n1+n2;
    n1=n2
    n2=n3
    print(n3)