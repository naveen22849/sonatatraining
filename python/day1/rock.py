while True:
    x=input('enter rock, paper,scissor')
    y=input('enter rock, paper, scissor')
    if x=='rock' and y=='paper':
        print('y wins')
    elif x=='rock' and y=='scissor':
        print('x wins')
    elif x=='paper' and y=='rock':
        print('x wins')
    elif x=='paper' and y=='scissor':
        print('y wins')
    elif x=='scissor' and y=='rock':
        print('y wins')
    elif x=='scissor' and y=='paper':
        print('x wins')
    elif x == 'scissor' and y == 'scissor':
        print("draw")
    elif x == 'rock' and y == 'rock':
        print("draw")
    elif x == 'paper' and y == 'paper':
        print("draw")
    else:
        print('invalid')