#Шифр Цезаря
# строчные
def za_shif_en(c, step):
    t = ''
    for i in c:
        if i in ' ,./*-+\';[]!@#$%^&*\()~"№;%:?':
            t += i
        else:
            if i in 'abcdefghijklmnopqrstuvwxyz':
                if (96 < (ord(i) + step) < 123):
                    t += chr(ord(i) + step)
                else:
                    t += chr((ord(i) + step) - 26)
            elif i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                if (64 < (ord(i) + step) < 90):
                    t += chr(ord(i) + step)
                else:
                    t += chr((ord(i) + step) - 26)
    return t
def za_shif_ru(c, step):
    t = ''
    for i in c:
        if i in ' ,./*-+\';[]!@#$%^&*\()~"№;%:?':
            t += i
        else:
            if i in 'абвгдежзийклмнопрстуфхцчшщъыьэюя':
                if (1071 < (ord(i) + step) < 1104):
                    t += chr(ord(i) + step)
                else:
                    t += chr((ord(i) + step) - 32)
            elif i in 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
                if (1039 < (ord(i) + step) < 1072):
                    t += chr(ord(i) + step)
                else:
                    t += chr((ord(i) + step) - 32)
    return t
def en_rashifr(c, step):
    q = 26 - step
    return za_shif_en(c, q)

def ru_rashifr(c, step):
    q = 32 - step
    return za_shif_ru(c, q)
alf = input('Введите алфавит ru/en: ')
c = input('Введите текст: ')
shifr = input('расшифровать/зашифровать: ')
step = int(input('Введите шаг: '))
if shifr.lower() == 'зашифровать':
    if alf == 'en':
        print(za_shif_en(c, step))
    if alf == 'ru':
        print(za_shif_ru(c, step))
else:
    if alf == 'en':
        print(en_rashifr(c, step))
        # for e in range(0, 26):
        #     print(en_rashifr(c, step - e))
    if alf == 'ru':
        # for e in range(0, 32):
        #     print(ru_rashifr(c, step - e))
        print(ru_rashifr(c, step))