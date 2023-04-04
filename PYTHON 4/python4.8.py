from time import sleep


def inversao(a,b):
    print(f'O primeiro valor digitado é \033[33m{a}\033[m e o segundo é \033[33m{b}\033[m')
    sleep(1)
    print('\033[32mInvertendo...\033[m')
    sleep(2)
    print(f'Agora, o primeiro valor é \033[33m{b}\033[m e o segundo valor é \033[33m{a}\033[m')


while True:
    n1 = int(input('Digite o 1° valor inteiro: '))
    n2 = int(input('Digite o 2° valor inteiro: '))
    inversao(n1,n2)
    resp = str(input('Deseja continuar? [S/N] ')).upper()[0].strip()
    if resp not in 'S':
        break
print('\033[31mObrigado por utilizar o programa!\033[m')
