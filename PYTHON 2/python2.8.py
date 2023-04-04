from time import sleep
from random import randint
perguntas = ['Telefonou para a vítima?','Esteve no local do crime?','Mora perto da vítima?',
'Devia para a vítima?', 'Já trabalhou com a vítima?']
respostas = []
print('=' * 14)
print('INTERROGATÓRIO')
print('=' * 14)
for i, p in enumerate(perguntas):
    print(p)
    print('[1 - Sim / 2- Não]')
    resp = randint(1,2)
    sleep(0.7)
    print(resp)
    respostas.append(resp)
    sleep(1)
if respostas.count(1) == 1 or respostas.count(1) == 0:
    print('SITUAÇÃO: \033[32mInocente!\033[m')
elif respostas.count(1) == 2:
    print('SITUAÇÃO: \033[34mSuspeito!\033[m')
elif respostas.count(1) == 3 or respostas.count(1) == 4:
    print('SITUAÇÃO: \033[33mCúmplice!\033[m')
elif respostas.count(1) == 5:
    print('SITUAÇÃO: \033[31mAssassino!\033[m')

