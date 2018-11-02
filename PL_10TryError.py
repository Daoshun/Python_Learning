try:
    file = open('tryerror.py','r+')
except Exception as e:
    print('there is no file named tryerror.py')
    response = input('do you want to create a new file? y or n')
    if response == 'y':
        file = open('tryerror.py','w')
    else:
        pass
else:
    file.write('tryerror.py')
file.close()

