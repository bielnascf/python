def soma(a,b):
    s = a + b
    return s


def subtraçao(a,b):
    s = a - b
    return s


def multiplicaçao(a,b):
    m = a * b
    return m


def divisao(a,b):
    d = a / b
    return d


def divisaointeira(a,b):
    di = a // b
    return di


def resto(a,b):
    r = a % b
    return r


n1 = 150
n2 = 15
print(f'Os números escolhidos foram {n1} e {n2}.')
som = soma(n1,n2)
sub = subtraçao(n1,n2)
multi = multiplicaçao(n1,n2)
div = divisao(n1,n2)
divisao_inteira = divisaointeira(n1,n2)
res = resto(n1,n2)
print(f'{n1} + {n2} = {som}')
print(f'{n1} - {n2} = {sub}')
print(f'{n1} x {n2} = {multi}')
print(f'{n1} / {n2} = {div}')
print(f'{n1} // {n2} = {divisao_inteira}')
print(f'RESTO = {res}')
