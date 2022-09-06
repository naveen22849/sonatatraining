number=int(input('enter the factorial number you want'))
fact=1
if(number<0):
    print('invalid number')
else:
    for i in range(1, number+1):
        fact=fact*i
    print(fact)