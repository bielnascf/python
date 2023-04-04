lista = []
valores = []
for c in range(1,11):
    n = int(input('Adicione um valor na lista: '))
    lista.append(n)
for valor in lista:
    if valor not in valores:
        valores.append(valor)
print(lista) 
print(valores)
print(f'Há {len(lista)} valores nessa lista.')
print(f'Há {len(valores)} valores diferentes nessa lista.')

