country = input('Where are you from? ').upper()
total = input('What total? ')
if country == 'CANADA':
    province  = input('Which province? ').upper()
    if province == 'ALBERTA':
        print('You must pay taxes ' + str(float(total)*0.05))
    elif province == 'ONTARIO' or province == 'NEW BRUNSWICK' or  province == 'NOVA SCOTIA':
        print('You must pay taxes ' + str(float(total)*0.13))
    else:
        print('You must pay taxes ' + str(float(total)*0.06))
else:
    print('You have any taxes')
