from random import randint
dado = []
for c in range(1,51):
    dado.append(randint(1,6))
print(dado)
if 6 in dado:
    percentual = (dado.count(6) * 100)/50
    print(f'O número 6 apareceu {dado.count(6)} vezes e seu percentual de aparição foi {percentual:.1f}%.')
