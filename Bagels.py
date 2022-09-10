import random
num_digit = 3
max_guess = 10
def main():
    print ('Привет! Это логическая игра, в которой надо угадать {}-х значное число,цифры в котором не повторяются.'.format(num_digit))
    print ("Есть {} попыток. Дается 3 типа подсказок:".format(max_guess))
    print ('Пико - цифра есть в загаданном числе, но не на своем месте.')
    print ('Ферми - цифра есть и она на своем месте')
    print ('Бейглз - цифры нет в загаданном числе.')
    counter = 1
    while True:
        print ('You have {} guesses left'.format(max_guess))
        number = get_number(num_digit)
        guessed_number = ''
        while counter <= max_guess:
            print ( 'Guess # {}'.format(counter))
            guessed_number = str(input("Загаданное число: "))
            clues = get_clues(number, guessed_number)
            print (clues)
            counter += 1
            if guessed_number == number:
                print ("You win!")
                break
            elif counter > max_guess:
                print ("You ran out of guesses")
                print ( 'The number was {}'.format(number))
                break
        print ("Want to continue? (y/n)")
        if not input() == 'y':
            break
        else:
            counter = 1
def get_number(z):
    number = ''
    numbers = list('1234567890')
    random.shuffle(numbers)
    for i in range(int(z)):
        number += numbers[i]
    return number
        
        
def get_clues(x, y):
    clues = []
    for i in range(len(x)):
        if y[i] == x[i]:
            clues.append('Fermi')
        elif y[i] in x:
            clues.append('Pico')
        elif y[i] not in x:
            clues.append('Bagels')
    clues.sort()
    return ' '.join(clues)
    
if __name__ == '__main__':
    main() 
    
    
            
        
