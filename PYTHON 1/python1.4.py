def comparaçao(x,y,l):
    s = 0
    if x > l:
        s = s + 1
    if y > l:
        s = s + 1
    print(f'Foram digitados {s} números maiores que o limite.')


a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))
limite = 8
comparaçao(a,b,limite)

