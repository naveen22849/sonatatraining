def friendbirthday():
    birthdays = {"Albert Einstein": "14/3/1889",
                 "Bill Gates": "28/10/1955",
                 "Steve Jobs": "24/2/1955"}
    print('Welcome to the birthday dictionary.')
    print('We know the birthdays of:')
    for i in birthdays:
        print(i)
    name = input("Who's birthday do you want to look up?")
    if name in birthdays:
        print(name , birthdays[name])

friendbirthday()


def num(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y

a = [1,2,3,4,3,2,1]
print(num(a))