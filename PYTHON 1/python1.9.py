def potencias(num):
    for c in range(num):
        c = c ** 2
        if 0 < c < num:
            print(c)


n = int(input('Digite um número: '))
potencias(n)

