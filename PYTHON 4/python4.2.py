def cabeçalho(txt):
    tam = len(txt) + 4
    print('=' * tam)
    print(f'  {txt}')
    print('=' * tam)


def linha():
    print('-' * 30)


def peso():
    s = 0
    for c in range(1,6):
        p = float(input(f'Peso da {c}° pessoa (kg): '))
        s = s + p
    if s > capacidade:
        cabeçalho(f'A soma dos pesos das pessoas foi de {s} kg, ultrapassando o limite de {capacidade} kg.')
        print('SITUAÇÃO: \033[31mNÃO LIBERADO\033[m')
    else:
        cabeçalho(f'A soma dos pesos das pessoas foi de {s} kg, sendo permitida a viagem.')
        print('SITUAÇÃO: \033[32mLIBERADO\033[m')


cabeçalho('ELEVADOR')
capacidade = float(input('Capacidade máxima (kg): '))
linha()
peso()
