sexo = str(input('Digite o seu sexo [F/M]: ')).strip().upper()[0]
while sexo not in 'FM':
    sexo = str(input('Resposta inválida. Digite o seu sexo [F/M]: '))
if sexo in 'FM':
    print(f'Sexo {sexo} registrado com sucesso.')
