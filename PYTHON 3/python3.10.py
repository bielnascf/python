a = float(input('Digite um valor: '))
b = float(input('Digite outro valor: '))
c = float(input('Digite outro valor: '))
print('''[0 < PAR < 10] MÉDIA ARITMÉTICA
[10 > ...] MÉDIA ARITMÉTICA E PONDERADA''')
i = int(input('Digite sua opção >> '))
if i % 2 == 0 and 0 < i < 10:
    aritmetica = (a + b + c)/3 
    print(f'A média aritmética é {aritmetica:.1f}.')
elif i >= 10:
    aritmetica = (a + b + c)/3
    ponderada = (2 * a + 3 * b + 4 * c)/9
    print(f'A média aritmética é {aritmetica:.1f}.')
    print(f'A média ponderada é {ponderada:.1f}.')
