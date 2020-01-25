r = int(input('Enter the number'))
w = r%2
if w == 0:
    print('even')
    if r>=10:
        print('super')
    else:
        print('oops')
elif w==1:
    print('odd')  
