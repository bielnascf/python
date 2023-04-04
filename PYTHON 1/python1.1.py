def classificaçao(num):
    if num > 0:
        print(f'O número {num} é positivo.')
    elif num == 0:
        print(f'O número {num} é neutro.')
    else:
        print(f'O número {num} é negativo.')


n = int(input('Digite um número: '))
classificaçao(n)
