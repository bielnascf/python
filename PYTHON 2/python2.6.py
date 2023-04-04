numeros = []
s = 0
m = 1
for c in range(1,6):
    n = int(input('Adicione um valor à lista: '))
    numeros.append(n)
    s = s + n
    m = m * n
print(f'A lista completa: {numeros}')
print(f'A soma dos valores na lista: {s}')
print(f'O produto dos valores na lista: {m}')
