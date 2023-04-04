cont = maior = menor = soma = 0
while True:
    n = int(input('Digite um valor (-1 para parar): '))
    cont = cont + 1
    soma = soma + n
    if n == -1:
        soma = soma + 1
        break
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print(f'A soma dos valores digitados foi {soma}.')
print(f'O menor valor digitado foi {menor}.')
print(f'O maior valor digitado foi {maior}.')
