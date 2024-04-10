#Угадайка слов
from random import*
print('Здравствуйте!')
print('Давайте играть в угадайку слов!')
word_list = ['труба', 'стакан', 'достижение', 'голос', 'гость', 'занятие', 'черта', 'господин', 'канал',
             'забота', 'угол', 'процедура', 'вкус', 'значение', 'статус', 'размер', 'сумма', 'свойство',
             'герой', 'поиск', 'условие', 'открытие', 'родственник', 'кожа', 'клуб', 'дыхание', 'существо',
             'предмет', 'обучение', 'очки', 'цена', 'минута', 'реклама', 'целое', 'мастер', 'содержание',
             'поездка', 'постель', 'конец', 'доктор', 'наличие', 'глава', 'поле', 'специалист', 'нога',
             'удивление', 'стол']
def get_word():
    return choice(word_list).upper()
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]
def alfas(n):
    if n.upper() in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
        return True
    return False
def play():
    t = 1
    guessed_words = []
    while True:
        if t == 1:
            if get_word() not in guessed_words:
                q = get_word()
            word_completion = '_' * len(q)
            guessed_letters = []
            tries = 6  # количество попыток
            c = list(word_completion)
            d = list(q)
            while tries > 0 and word_completion != q:
                print(f'Ваше количество попыток: {tries}')
                print(display_hangman(tries))
                print(word_completion)
                print('Вы вводили буквы:', *guessed_letters)
                print('Вы вводили слова:', *guessed_words)
                n = input('Введите букву: ').upper()
                while alfas(n) == False:
                    print('А может быть все-таки введем букву?')
                    n = input('Введите букву: ').upper()
                if n not in guessed_letters:
                    guessed_letters.append(n)
                else:
                    while n in guessed_letters:
                        print('Вы уже вводили эту букву!')
                        n = input('Введите букву: ').upper()
                if n in d:
                    while n in d:
                        e = d.index(n)
                        del c[e]
                        del d[e]
                        d.insert(e, ' ')
                        c.insert(e, n)
                else:
                    tries -= 1
                word_completion = ''.join(c)
                print(word_completion)
                if word_completion == q and tries != 0:
                    print('ПОЗДРАВЛЯЮ! ВЫ ВАИГРАЛИ!!!')
                    g = input('Вы хотите продолжить играть? да/нет: ')
                    guessed_words.append(q)
                    if g == 'нет':
                        t = 0
                        break
                if tries == 0:
                    print('Вы проиграли...')
                    print(f'Я загадал слово {q}')
                    g = input('Вы хотите продолжить играть? да/нет: ')
                    guessed_words.append(q)
                    if g == 'нет':
                        t = 0
                        break

        else:
            break
    print()
    print('До свидания!')
play()