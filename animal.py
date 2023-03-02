import sys

def lion():
    print('roar')
    
def cat():
    print('Meow')

def dog():
    print('baw')

def default():
    print('Hellp')

def main():
    if sys.argv[1] == 'cat':
        cat()
    elif sys.argv[1] == 'dog':
        dog()
    elif sys.argv[1] == 'lion':
        lion()
    else:
        default()

if __name__ == '__main__':
    main()
