#Шифр Цезаря
def za_shif_en(c):
    t = ''
    f = []
    for l in c:
        step = len(l)
        for i in l:
            if i in ',./*-+\';[]!@#$%^&*\()~"№;%:?':
                t += i
            if i == ' ':
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
        f.append(t)
    return f[-1]
c = input().split()
w = []
for y in c:
    r = ''
    if y[0] in ',./*-+\';[]!@#$%^&*\()~"№;%:?':
        w.append(y[0])
    for k in y:
        if k not in ',./*-+\';[]!@#$%^&*\()~"№;%:?':
            r += k
    w.append(r)
    if k in ',./*-+\';[]!@#$%^&*\()~"№;%:?':
        w.append(k)
    w.append(' ')
print(za_shif_en(w))
