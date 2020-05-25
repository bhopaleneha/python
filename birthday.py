birthdays = {'sourabh bhaya':'june 13 1996','sunny bhaya':'october 7 1988','piyush bhaya ':'august 5 1992'}
while True:
    print('enter a name :  (press only enter to close)' )
    name=input()
    if name =='':
        break
    if name in birthdays:
        print(birthdays[name]+ ' is the birthday of '+name)
    else:
        print('sorry i do not have birthday info for'+name)
        print('what is there birthday')
        bday=input()
        birthdays[name]=bday
        print('birthday database updated')
