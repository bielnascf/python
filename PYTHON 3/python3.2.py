from time import sleep


def comparaçao(a,b):
    print(f'Você digitou os valores \033[32m{a}\033[m e \033[32m{b}\033[m.')
    sleep(1)
    print('\033[32mAnalisando...\033[m')
    sleep(2)
    if a == b:
        print('\033[33mOs valores digitados são iguais.\033[m')
    else:
        print('\033[31mOs valores digitados são diferentes.\033[m')


n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
comparaçao(n1,n2)
print('FIM DO PROGRAMA')
