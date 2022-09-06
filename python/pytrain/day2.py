def age(a):
    num = 100 - a
    return num



def count(n):
    new = n.split()
    return len(new)



def palindrome(num):
    num = input('enter the number to check if its palindrome: ')
    if num==num[::-1]:
        p='palindrome'
        return p
    else:
        p='not a palindrome'
        return p




def game(x, y):
    x = input('enter rock, paper,scissor')
    y = input('enter rock, paper, scissor')
    if x == 'rock' and y == 'paper':
        p = 'y wins'
    elif x == 'rock' and y == 'scissor': \
            p = 'x wins'
    elif x == 'paper' and y == 'rock': \
            p = 'x wins'
    elif x == 'paper' and y == 'scissor':
        p = 'y wins'
    elif x == 'scissor' and y == 'rock':
        p = 'y wins'
    elif x == 'scissor' and y == 'paper':
        p = 'x wins'
    elif x == 'scissor' and y == 'scissor':
        p = "draw"
    elif x == 'rock' and y == 'rock':
        p = "draw"
    elif x == 'paper' and y == 'paper':
        p = "draw"
    else:
        p = 'invalid'
    return p





def largestnumber(n1,n2,n3):
    if n1>=n2 and n1>=n3:
        largest=n1
    elif n2>=n1 and n2>=n3:
        largest=n2
    else:
        largest=n3
    return largest


