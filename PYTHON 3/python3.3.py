from time import sleep


def resultado(num):
    print(f'Você digitou o número \033[32m{num}\033[m.')
    sleep(1)
    print('\033[33mAnalisando...\033[m')
    sleep(2)
    if num > 0:
        print('O número digitado é \033[32mPOSITIVO\033[m.')
    elif num == 0:
        print('O número digitado foi 0 e por isso é \033[34mNEUTRO\033[m')
    elif num < 0:
        print('O número digitado é \033[31mNEGATIVO\033[m')


def cabeçalho(txt):
    tam = len(txt) + 4
    print('-' * tam)
    print(f'  {txt}')
    print('-' * tam)


while True:
    try:
        n = int(input('Digite um número: '))
    except:
        print('\033[31mTivemos um problema... O número digitado não é um número inteiro.\033[m')
    else:
        resultado(n)
    finally:
        resp = str(input('Tentar novamente? [S/N]  ')).upper()[0].strip()
        if resp not in 'S':
            break
cabeçalho('\033[31mFIM DO PROGRAMA. Volte sempre!\033[m')
