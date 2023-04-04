def cabeçalho(txt):
    tam = len(txt) + 4
    print('-' * tam)
    print(f'  {txt}')
    print('-' * tam)


def fibonacci():
    t1 = 0
    t2 = 1
    print(f'\033[32m{t1}\033[m -> \033[32m{t2}\033[m', end = '')
    cont = 3
    while cont <= n:
        t3 = t1 + t2
        print(f' -> \033[32m{t3}\033[m', end = '')
        t1 = t2
        t2 = t3
        cont = cont + 1
    print(' -> \033[31mFIM\033[m')


cabeçalho('SEQUÊNCIA DE FIBONACCI')
n = int(input('Quantos termos mostrar na sequência?: '))
fibonacci()
