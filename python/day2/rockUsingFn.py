def game(x, y):

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
x = input('enter rock, paper,scissor')
y = input('enter rock, paper, scissor')

print(game(x,y))
