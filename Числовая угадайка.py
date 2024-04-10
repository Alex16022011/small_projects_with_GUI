#Числовая угадайка
def is_valid(n):
    if n > 100 or n < 0:
        return False
from random import*
d = []
counter = 0
print('Здравствуйте!')
print()
print('Добро пожаловать в числовую угадайку')
print()
while True:
    c = randint(1, 100)
    trying = 5
    while trying != 0:
        n = int(input('Введите любое число от 0 до 100: '))
        while True:
            if is_valid(n) == False:
                print('А может быть все-таки введем целое число от 1 до 100?')
                print()
                n = int(input('Введите любое число от 0 до 100: '))
            else:
                break
        print()
        if n == c:
            print('Вы угадали, поздравляем!')
            counter += 1
            print(f'Ваш счет: {counter}')
            print()
            break
        elif n > c:
            print('Ваше число больше загаданного, попробуйте еще разок')
            trying -= 1
            print(f'У вас осталось {trying} попытки')
            print()
        else:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            trying -= 1
            print(f'У вас осталось {trying} попытки')
            print()
    print()
    if trying == 0:
        print('Вы проиграли...')
        print(f'Я загадал число {c}')
        break
    print()
    o = input('Скажите, вы хотите сыграть еще раз да/нет: ')
    if o != 'да':
        break
print('Оставьте свой отзыв об этой игре:')
print()
d.append(input('Отзыв: '))
print()
if len(d) > 0:
    q = input('Хотите посмотреть другие отзывы да/нет: ')
    print()
    if q == 'да':
        print(*d, sep = '\n')
print()
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')