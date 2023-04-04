vet = []
pos = []
semdup = []
for c in range(1,11):
    n = int(input('Adicione um valor inteiro à lista: '))
    vet.append(n)
    if n > 0:
        pos.append(n)
print(f'A lista completa: {sorted(vet)}')
print(f'A lista apenas com valores positivos: {sorted(pos)}')
for vetor in pos:
    if vetor not in semdup:
        semdup.append(vetor)
print(f'A lista apenas com os valores positivos não repetidos: {sorted(semdup)}')
