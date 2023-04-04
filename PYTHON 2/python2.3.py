lista = [[]]
for c in range(1,5):
    n = int(input('Adicione um valor a lista: '))
    lista.append(n)
    if n % 2 == 0:
        lista[0].append(n)
print(lista)
if 9 in lista:
    print(f'O número 9 aparece {lista.count(9)} vez(es).')
else:
    print('O número 9 não aparece na lista.')
for i,v in enumerate(lista):
    if v == 3:
        print(f'A posição do primeiro valor 3 é {i}. ')
print(f'Os numéros pares digitados foram {lista[0]}.')
