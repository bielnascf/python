prov = []
princ = []
while True:
    print('-=' * 30)
    prov.append(str(input('Digite o seu nome: ')).strip().title())
    prov.append(int(input('Digite sua idade: ')))
    prov.append(float(input('Digite sua altura: ')))
    princ.append(prov[:])
    prov.clear()
    print('-=' * 30)
    resp = str(input('Deseja continuar? [S/N] ')).upper()[0].strip()
    if resp == 'N':
        break
print(sorted(princ, reverse = True))

