import time
time.sleep(1)
print('Welcome to the TBADPII (Text Based Adventure Development Project II).')
time.sleep(1)
name = input('What is your name? ')
time.sleep(1)
print('[???]> Hello, ' + name + '. This is the tutorial for the TBADPII.')
time.sleep(1)
print('[???]> A decision screen is below. This is how the game changes and develops based on your decisions.')
print('DECISIONS')
print('---------')
print('1. -Say hi')
print('2. -Run away')
time.sleep(1)
print('[???]> A quick note: Even if you input 2, the game will continue as if you put in 1.')
time.sleep(1)
input('What choice will you make? ')
print('[???]> I assume you put 1 or 2; even if you had input "banananaaaaaa" or something equally foolish, it would still show this text. Now, for the real challenge.')
time.sleep(3)
print('[' + name + ']> TURTLE!!! I mean, uh... Huh? Where am I?')
print('DECISIONS')
print('---------')
print('1. -Explore north')
print('2. -Explore south')
choice = input('What choice will you make? ')
time.sleep(1)
if choice == '1':
    print('')
elif choice == '2':
    print('')  
