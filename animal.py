import sys

def dog():
    print('baw')

def default():
    print('Hellp')

def main():
    if sys.argv[1] == 'dog':
        dog()
    else:
        default()

if __name__ == '__main__':
    main()
