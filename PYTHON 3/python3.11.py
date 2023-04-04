letra = str(input('Digite uma letra: ')).upper().strip()
while len(letra) > 1 or letra.isnumeric():
    letra = str(input('Resposta inválida. Digite apenas uma letra do alfabeto: ')).upper().strip()
if letra not in 'AEIOU':
    print(f'A letra {letra} é uma consoante.')
else:
    print(f'A letra {letra} é uma vogal.')
