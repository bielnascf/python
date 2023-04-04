def bissexto(a):
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        return True
    else:
        return False

while True:
    ano = int(input('Digite um ano aleatório e direi se é bissexto: '))
    bissexto(ano)
    bi = bissexto(ano)
    print(bi)
    resp = input('Deseja continuar? [S]/[N] ').upper()[0].strip()
    if resp in 'N':
        break
print('Programa Finalizado.')
