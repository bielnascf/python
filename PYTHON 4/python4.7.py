def maiorvalor():
    for c in range(1,4):
        n = int(input(f'Digite o {c}° número: '))
        if c == 1:
            maior = n
        else:
            if n > maior:
                maior = n
    print(f'O maior número digitado foi {maior}')


while True:
    maior = 0
    maiorvalor()
    resp = str(input('Deseja Continuar? [S/N] ')).upper()[0].strip()
    if resp not in 'S':
        break
    
print('Obrigado, volte sempre!')
