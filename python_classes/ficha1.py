def linha():
    print('-=' * 30)    


def tabela():
    for pos in range(0, len(produtos)):
        if pos % 2 == 0:
            print(f'{produtos[pos]:<30}',end = '')
        else:
            print(f'R${produtos[pos]:>7.2f}')


def tabela_desconto():
    while True:
        percentual = float(input('Digite o percentual de desconto que deseja aplicar (Digite 0 para parar): '))
        if percentual == 0:
            break
        for pos in range(0, len(produtos)):
            if pos % 2 == 0:
                print(f'{produtos[pos]:<30}',end = '')
            else:
                produtos[pos] = produtos[pos] - ((produtos[pos] * percentual)/100)
                print(f'R${produtos[pos]:>7.2f}')


produtos = []

while True:
    linha()
    try:
        cod = int(input('Código do produto: '))
        des = str(input('Nome do produto: ')).title().strip()
        produtos.append(des)
        pre = float(input('Preço do produto: '))
        produtos.append(pre)
    except:
        print('\033[31mOops... Um erro foi encontrado.\033[m')
    else:
        resp = str(input('Continuar? [S]/[N] ')).upper()[0].strip()
        while resp not in 'SN':
            resp = str(input('Resposta inválida. Deseja continuar? [S]/[N] ')).upper()[0].strip()
        if resp == 'N':
            break

linha()
tabela()
linha()
tabela_desconto()
linha()
