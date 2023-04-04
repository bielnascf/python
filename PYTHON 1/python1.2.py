while True:
    print('-=' * 20)
    print('''[1] Inteiro absoluto
[2] Flutuante absoluto
[3] Sair''')
    print('-=' * 20)
    opc = int(input('Escolha sua opção >> '))
    if opc == 1:
        n = int(input('Digite um valor inteiro: '))
        abso = abs(n)
        print(f'O valor absoluto do número {n} é {abso}.')
    elif opc == 2:
        n = float(input('Digite um valor flutuante: '))
        abso = abs(n)
        print(f'O valor absoluto de {n} é {abso}')
    elif opc == 3:
        print('Saindo...')
        break
print('Programa Finalizado.')
