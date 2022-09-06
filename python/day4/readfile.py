filename=input('enter the file name:')
try:
    f=open(filename,"r")
    print(f.read())
    f.close()
except FileNotFoundError:
    print('error file name not found')