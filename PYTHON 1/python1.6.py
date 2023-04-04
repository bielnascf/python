def indice(lis, lim):
    for i, v in enumerate(lis):
        if v >= lim:
            print(f'Valor maior que o limite no indice {i}')


lista = []
limite = 10
while True:
    print('-=' * 20)
    n = int(input('Adicione um valor à lista: '))
    lista.append(n)
    sorted(lista)
    resp = str(input('Deseja continuar? [S]/[N] ')).upper()[0].strip()
    if resp in 'N':
        break
print('-=' * 20)
lista.sort()
print(lista)
indice(lista, limite)
