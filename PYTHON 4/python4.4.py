def bissexto(a):
    if a % 400 == 0 or a % 4 == 0 and a % 100 != 0:
        print('Esse ano é bissexto!')
    else:
        print('Esse ano não é bissexto.')


r = 'S'
while True:
    ano = int(input('Digite um ano e direi se ele é bissexto: '))
    bissexto(ano)
    r = str(input('Quer continuar? ')).strip().upper()[0]
    if r == 'N':
        break
