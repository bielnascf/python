from random import randint
valores = []
quantidade = []
s1 = s2 = s3 = s4 = s5 = s6 = 0
for c in range(1,11):
    dado = randint(1,6)
    valores.append(dado)
print(valores)
for n in range(1,7):
    quantidade.append(valores.count(n))
print(quantidade)
