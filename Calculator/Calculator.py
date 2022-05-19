print('\nWelcome to a Calculator App built by Ebube Okoli.')
print('____________________________________________________')
result = 0
attempts = 0

def addition(result = ''):
    sums = result if result != '' else []
    count = 1 if result != '' else 0
    while True:
        number = input('Enter the next number to add. \n Press \'Enter\' if you do not want to enter another number: ' 
        if count >= 1 else 'Enter the first number to add: ')

        if number == '':
            break
        else :
            sums += float(number)
            count += 1

    return sums


def subtraction(result = ''):
    numbers_to_sub = [result] if result != '' else []
    count = 1 if result != '' else 0
    while True:
        if count >= 2:
            break

        number = input('Enter the number to subtract. \n Press \'Enter\' if you do not want to enter another number: ' 
        if count >= 1 else 'Enter the number to subtract from: ')

        
        numbers_to_sub.append(float(number) if number != '' else 0)
        count = count + 1 if number != '' else 2
    
    return numbers_to_sub[0] - numbers_to_sub[1]

def multiply(result = ''):
    solution = result if result != '' else 1
    count = 1 if result != '' else 0

    while True:
        if count >= 2:
            break

        number = input('Enter the next number to multiply. \n Press \'Enter\' if you want to default to one: ' 
        if count >= 1 else 'Enter the first number to multiply : ')

        
        solution *= float(number) if number != '' else 1
        count = count + 1 if number != '' else 2

    return solution

def divide(result = ''):
    numbers = [result] if result != '' else []
    count = 1 if result != '' else 0

    while True:
        if count >= 2:
            break

        number = input('Enter the number to divide by. \n Press \'Enter\' if you want to default to one: ' 
        if count >= 1 else 'Enter the number to divide: ')

        
        numbers.append(float(number) if number != '' else 0)
        count = count + 1 if number != '' else 2

    return numbers[0]/numbers[1]


def modulus(result = ''):
    numbers = [result] if result != '' else []
    count = 1 if result != '' else 0

    while True:
        if count >= 2:
            break

        number = input('Enter the number to mod by. \n Press \'Enter\' if you want to default to one: ' 
        if count >= 1 else 'Enter the number you want to find its modulus: ')

        
        numbers.append(float(number) if number != '' else 0)
        count = count + 1 if number != '' else 2

    return numbers[0]%numbers[1]


        


while True:
    options = input('\nUse previous result? (Y/N): ').lower() if attempts > 0 else 'n'

    while options != 'y' and options != 'n':
        print('Invalid Selection. Try again.')
        options = input('\nUse previous result? (Y/N): ').lower()

    choice = input('\nWhat would you like to do? \n A - Add \n S - Subtract \n M - Multiply \n D - Divide \n P - Modulus \n').lower()
    

    if choice == 'a':
        result = addition(result if options == 'y' else '')

    elif choice == 's':
        result = subtraction(result if options == 'y' else '')

    elif choice == 'm':
        result = multiply(result if options == 'y' else '')

    elif choice == 'd':
        result = divide(result if options == 'y' else '')

    elif choice == 'p':
        if options == 'y' and (int(result) != result) :
            print('Your previous result is in decimal and can not be used to compute a modulus')
        else:
            result = modulus(result if options == 'y' else '')

    else:
        print('You have made an invalid selection. Try again')
        continue
    
    print('Your result is ', result)
    attempts += 1

    repeat = input('\nDo you want to do another calculation? (Y/N): ').lower()

    while repeat != 'y' and repeat != 'n':
        print('Invalid Selection. Try again.')
        repeat = input('\nDo you want to do another calculation? (Y/N): ').lower()

    if repeat == 'y':
        continue
    else:
        print('____________________________________________________')
        print('\nThank you for trying out my calculator application.')
        break

