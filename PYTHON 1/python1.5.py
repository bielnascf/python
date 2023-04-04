def conceito(n):
    if 9 < n <= 10:
        print(f'NOTA: \033[32m{n}\033[m')
        print('CONCEITO: \033[32mA\033[m')
    elif 7 <= n <= 8.9:
        print(f'NOTA: \033[33m{n}\033[m')
        print('CONCEITO: \033[33mB\033[m')
    elif 5 <= n <= 6.9:
        print(f'NOTA: \033[34m{n}\033[m')
        print('CONCEITO: \033[34mC\033[m')
    elif 4.5 <= n <= 4.9:
        print(f'NOTA: \033[35m{n}\033[m')
        print('CONCEITO: \033[35mD\033[m')
    elif n < 4.5:
        print(f'NOTA: \033[31m{n}\033[m')
        print('CONCEITO: \033[31mF\033[m')


nota = float(input('Digite a nota do aluno: '))
while nota > 10 or nota < 0:
    nota = float(input('\033[31mNota inválida\033[m. Digite a nota do aluno: '))
conceito(nota)
