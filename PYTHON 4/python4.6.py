def vogal_ou_consoante(l):
    if l in 'AEIOU':
        print(f'A letra {l} é uma vogal.')
    else:
        print(f'A letra {l} é uma consoante.')


while True:
    letra = str(input('Digite uma letra e direi se é uma vogal ou consoante: ')).upper().strip()
    vogal_ou_consoante(letra)
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp not in 'S':
        break
print('Obrigado por usar o programa, volte sempre!')
