def condiçao(x,y,l):
    if x + y > l:
        return True
    else:
        return False


limite = 25
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
condiçao(a,b,limite)
c = condiçao(a,b,limite)
print(c)
