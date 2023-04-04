somap = somaq = somai = somaqi = 0
for p in range(2, 101):
    if p % 2 == 0:
        somap = somap + p
    else:
        somai = somai + p
for q in range(1, 101):
    somaq = somaq + (q^2)
    if (q^2) % 2 != 0:
        somaqi = somaqi + q
totalab = somaqi + somai
print(f'A soma de todos os números pares de 2 a 100 é {somap}.')
print(f'A soma de todos os quadrados entre 1 e 100 é {somaq}.')
print(f'A soma entre de todos os números ímpares entre as condições anteriores é {totalab}.')
somadig = 0
n = int(input('Digite um número: '))
s = str(n)
for num in range(0, len(s)):
    if int(s[num]) % 2 != 0:
        somadig = somadig + int(s[num])
print(f'A soma de cada digito ímpar do número digitado é {somadig}')
