from time import sleep


def situaçao(s, d):
    saldo = salario - despesas
    if saldo >= 0:
        print(f'Salário: {s}')
        print(f'Gastos: {d}')
        print(f'Saldo: \033[32m{saldo}\033[m')
        print('Situação: \033[32mGastos dentro do orçamento\033[m')
    elif saldo < 0:
        print(f'Salário: {s}')
        print(f'Gastos: {d}')
        print(f'Saldo: \033[31m{saldo}\033[m')
        print('Situação: \033[31mOrçamento estourado\033[m.')


while True:
    try:
        salario = float(input('Digite o seu salário: '))
        despesas = float(input('Digite o valor total das suas despesas: '))
    except:
        print('Encontramos um erro! Digite novamente.')
    else:
        situaçao(salario, despesas)
    finally:
        resp = str(input('Fazer novamente? [S/N] ')).upper()[0].strip()
        if resp not in 'S':
            print('\033[33mFinalizando...\033[m')
            sleep(2)
            print('\033[31mPrograma finalizado. Volte sempre!\033[m')
            break
