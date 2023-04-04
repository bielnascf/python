lista = []
n = 4
for c in range(n):
    lista.append(float(input('Adicione valores à lista: ')))
soma = 0
for c in range(n):
    soma = soma + lista[c]
media = soma/n
distmin = -1
distmin_pos = -1
for i in range(0,n):
    dif = 0
    if lista[i] >= media:
        dif = lista[i] - media
    else:
        dif = media - lista[i]
    if distmin == -1 or dif < distmin:
        distmin = dif
        distmin_pos = i
print(f'Vetor: {lista}')
print(f'Média: {media:.1f}')
print(f'Valor mais próximo da média: {lista[distmin_pos]}')
