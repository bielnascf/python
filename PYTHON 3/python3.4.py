from time import sleep


def cabeçalho(txt):
    tam = len(txt)
    print('=' * tam)
    print(f'{txt}')
    print('=' * tam)


def opçoes():
    while True:
        sleep(1)
        cabeçalho('''[1] Contagem vertical
[2] Contagem Horizontal
[3] Finalizar programa''')
        resp = int(input('Escolha a sua opção >> '))
        if resp == 1:
            for c in range(1,21):
                print(c)
        elif resp == 2:
            for c in range(1,21):
                print(c, end=' ')
        elif resp == 3:
            print('\033[33mFinalizando...\033[m')
            sleep(2)
            print('\033[31mPrograma finalizado. Volte sempre!\033[m')
            break




cabeçalho('SISTEMA DE CONTAGEM')
opçoes()



