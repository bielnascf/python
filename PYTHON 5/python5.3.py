import datetime


def data(d,m,a):
    print(f'Data do seu nascimento: {d}/{m}/{a}')


dia = int(input('Digite o dia do seu nascimento: '))
while dia > 31 or dia < 1:
    dia = int(input('Resposta inválida. Digite o dia do seu nascimento: '))
mes = int(input('Digite o mês do seu nascimento: '))
while mes > 12 or mes < 1:
    mes = int(input('Resposta inválida. Digite o mês do seu nascimento: '))
ano = int(input('Digite o ano do seu nascimento: '))
while ano > datetime.date.today().year:
    print('Não mete essa, nem chegamos nesse ano ainda!')
    ano = int(input('Digite o ano do seu nascimento: '))
data(dia,mes,ano)
