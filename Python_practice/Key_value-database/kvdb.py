db = {}
print('Welcome to the simplest key-value database')
while True:
    print('What do you want to do?')
    print('Enter P to [P]ut, G to [G]et or L to [L]ist')
    print('Or enter Q to [Q]uit')
    action = input().lower()
    if action == 'p':
        k = input('Enter key: ')
        d = input('Enter data: ')
        db[k] = d
    elif action == 'g':
        k = input('Enter key: ')
        if not k in db:
            print('No such key')
        else:
            print('Your data: %s' % db[k])
    elif action == 'l':
        print('DB contents:')
        print(db)
    elif action == 'q':
        print('Bye')
        break
