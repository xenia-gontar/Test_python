
text = input("Введите алгебраическое выражение: ")

x_count = 0
y_count = 0
z_count = 0
free_count = 0

expression = list(text)
expression.append("@")
number = ''
for i in range(0, len(expression)):
    print(f'Текущий символ - {expression[i]}')
    if expression[i] in ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'):
        number =  number + expression[i]
        print("число")
        print(number)
    elif expression[i] == 'x':
        if number == '':
            number = '1'
        x_count = x_count + int(number)
        print("x")
        print(number)
        number = ''
    elif expression[i] == 'y':
        print("y")
        print(number)
        if number == '':
            number = '1'
        y_count = y_count + int(number)
        number = ''
    elif expression[i] == 'z':
        print("z")
        print(number)
        if number == '':
            number = '1'
        z_count = z_count + int(number)
        number = ''
    elif expression[i] in ('-', '+'):
        if number != '':
            free_count = free_count + int(number)
        number = ''
        if expression[i] == '-':
            number = expression[i]
    elif expression[i] == '@':
        if number != '':
            free_count = free_count + int(number)
            
print(x_count, y_count, z_count, free_count)    
