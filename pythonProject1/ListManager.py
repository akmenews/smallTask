label = '''                  menu 
    1. show list
    2. add item
    3. remove item by position
    4. remove item by value
    5. save list
    0. exit
    '''
command = input('enter command number')
data = []
while command != '0':
    if command == '1':
        print (data)
    elif command == '2':
        item = input ('enter item')
        if item:
            data.append(item)
    elif command == '3':
        position = input('enter remove position ')
        if position.isdigit():
            position = int(position) - 1
            if 0 < position < len(data):
                data.pop(position)
            else:
                print('wrong position ')
    if command == '4':
        value = input('enter value ')
        if value:




    command = input('enter command number')

