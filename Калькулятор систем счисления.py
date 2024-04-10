print('Здравствуйте!')
print()
print('Я калькулятор систем счисления')
print()
cv = 1
while cv == 1:
    a = input('Введите число: ').upper()
    print()
    for i in a:
        if i == '-':
            up = 1
            a = a[1:]
        else:
            up = 0
            a = a[:]
    counter = 0
    for i in a:
        if i in '0123456789':
            counter += 1
        if counter == len(a):
            a = int(a)
    b = int(input('Введите систему счисления в которую хотите перевести число: 1-64: '))
    print()
    q = str(a)[::-1]
    p = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
         27,
         28, 29,
         30, 31, 32, 33, 34, 35, 36]
    z = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F',
         'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']
    if b == 10:
        c = int(input(f'Введите систему счисления числа {a}: '))
        if c < 10:
            d = 0
            for j in range(len(q)):
                w = q[j]
                d += (int(w) * (c ** j))
            print()
            if up == 1:
                print(f'Число -{a} (система счисления {b}) = -{d}')
            else:
                print(f'Число {a} (система счисления {b}) = {d}')
            print()
        else:
            if c > 10:
                c = 16
                u = z[:c]
                h = p[:c]
                q = []
                for i in a:
                    if i in '0123456789':
                        q.append(i)
                    else:
                        q.append(i)
                new = []
                for l in q:
                    if l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        ind = u.index(l)
                        new.append(h[h.index(ind)])
                    else:
                        new.append(int(l))
                d = 0
                counter = len(new) - 1
                for j in range(len(new)):
                    w = new[j]
                    d += (int(w) * (c ** (counter - j)))
                if up == 1:
                    print(f'Число -{a} (система счисления {b}) = -{d}')
                else:
                    print(f'Число {a} (система счисления {b}) = {d}')
                print()
    else:
        if b < 10:
            f = []
            for i in range(64):
                y = a
                c = ''
                while y >= b:
                    t = y % b
                    c += str(t)
                    y //= b
                c += str(y % b)
                q = c[::-1]
                f.append(q)
            if up == 1:
                print(f'Число -{a} (система счисления {b}) = -{f[-1]}')
            else:
                print(f'Число {a} (система счисления {b}) = {f[-1]}')
            print()
        if b > 10:
            f = []
            y = a
            we = ''
            while y >= b:
                t = y % b
                if t not in p:
                    we += str(t)
                else:
                    r = p.index(t)
                    we += z[r]
                y //= b
            we += str(y)
            q = we[::-1]
            f.append(q)
            if up == 1:
                print(f'Число -{a} (система счисления {b}) = -{f[-1]}')
            else:
                print(f'Число {a} (система счисления {b}) = {f[-1]}')
            print()
    ym = input('Вы хотите продолжить? да/нет: ')
    if ym == 'нет':
        cv = 0
print('До свидания!')