def letrastotal(txt):
    qnt = len(txt) - txt.count(' ')
    return qnt

def letrasprimeironome(lista):
    qnt = len(lista[0])
    return qnt


def cabeçalho(txt):
    tam = len(txt) + 4
    print('-' * tam)
    print(txt)
    print('-' * tam)


nome = str(input('Digite o seu nome completo: ')).strip().title()
print(f'Seu nome completo é {nome}')
n = nome.split()
quantidade1 = letrastotal(nome)
quantidade2 = letrasprimeironome(n)
cabeçalho('  Algumas informações sobre o seu nome:')
print(f'Nome em letras maiúsculas: {nome.upper()}')
print(f'Nome em letras minúsculas: {nome.lower()}')
print(f'Quantidade de letras: {quantidade1}')
print(f'Quantidade de letras do seu primeiro nome: {quantidade2}')
