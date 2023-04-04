from time import sleep


def cabeçalho(txt):
    tam = len(txt)
    print('=' * tam)
    print(txt)
    print('=' * tam)


def linha():
    print('-' * 50)


def mediafinal(a,b):
    mf = (a + b)/2
    return mf


cabeçalho('NOTAS DO PRIMEIRO BIMESTRE')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m1 = (n1 + n2) / 2
cabeçalho('NOTAS DO SEGUNDO BIMESTRE')
n3 = float(input('Digite a primeira nota: '))
n4 = float(input('Digite a segunda nota: '))
m2 = (n3 + n4) / 2
linha()
print(f'{"CALCULANDO...":^50}')
linha()
media_final = mediafinal(m1,m2)
sleep(2)
print(f'As notas do primeiro trimestre foram: {n1} e {n2}')
print(f'Média: {m1:.1f}')
linha()
print(f'As notas do segundo trimestre foram: {n3} e {n4}')
print(f'Média: {m2:.1f}')
linha()
print(f'MÉDIA FINAL: {media_final:.1f}')
