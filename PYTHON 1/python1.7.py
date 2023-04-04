def soma(num):
    s = 0
    for c in range(num):
        if 0 < c <= num:
            s = s + c
    return s


n = int(input('Digite um número: '))
somanumeros = soma(n)
print(f'A soma de todos os números menores ou iguais a {n} é {somanumeros}.')
