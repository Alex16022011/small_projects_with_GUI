#Генератор безопасных паролей
from random import*
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
neod = 'il1Lo0O'
chars = ''
print('Здравствуйте!')
print()
print('Меня зовут "Генератор безопасных паролей')
print()
counter_parols = int(input('Введите количество нужных вам паролей: '))
print()
leng = int(input('Введите длину одного пароля: '))
print()
dig = input('Включать ли цифры? да/нет: ')
print()
letter1 = input('Включать ли строчные буквы? да/нет: ')
print()
letter2 = input('Включать ли прописные буквы? да/нет: ')
print()
punk = input('Включать ли символы? да/нет: ')
print()
neo = input('Исключать ли неоднозначные символы (il1Lo0O)? да/нет: ')
print()
repete = input('Исключить ли повторы? да/нет: ')
if dig == 'да':
    chars += digits
if letter1 == 'да':
    chars += lowercase_letters
if letter2 == 'да':
    chars += uppercase_letters
if punk == 'да':
    chars += punctuation
if neo == 'да':
    chars += neod
if repete == 'да':
    def generate_password(length, chars):
        q = ''
        for i in range(length):
            c = choice(chars)
            if c not in q:
                q += c
        return q
else:
    def generate_password(length, chars):
        q = ''
        for i in range(length):
            q += choice(chars)
        return q
print()
print('Ваши пароли:')
print()
for _ in range(counter_parols):
    print(generate_password(leng, chars))