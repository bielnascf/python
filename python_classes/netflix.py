from time import sleep
class Cliente():
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['Basic', 'Premium']
        if plano == 1:  
            self.plano = self.lista_planos[0]
        elif plano == 2:
            self.plano = self.lista_planos[1]
        else:
            print('\033[31mPlano Inválido.\033[m')
    
    def mudar_plano(self, novo_plano):
        if novo_plano == 1:
            self.plano = self.lista_planos[0]
        elif novo_plano == 2:
            self.plano = self.lista_planos[1]
        else:
            print('\033[31mPlano inválido.\033[m')
    
    def ver_filme(self, filme, plano_cliente):
        self.lista_filmes = ['Fast and Furious 9', 'The Babadook', 'The conjuring']
        if filme == 1 and plano_cliente == 'Premium':
            print(f'Ver filme {self.lista_filmes[0]} 1080p HD 4K')
        elif filme == 1 and plano_cliente == 'Basic':
            print(f'Ver filme {self.lista_filmes[0]} 480p Not HD')
        if filme == 2 and plano_cliente == 'Premium':
            print(f'Ver filme {self.lista_filmes[1]} 1080p HD 4K')
        elif filme == 2 and plano_cliente == 'Basic':
            print(f'Ver filme {self.lista_filmes[1]} 480p Not HD')
        if filme == 3 and plano_cliente == 'Premium':
            print(f'Ver filme {self.lista_filmes[2]} 1080p HD 4K')
        elif filme == 3 and plano_cliente == 'Basic':
            print(f'Ver filme {self.lista_filmes[2]} 480p Not HD')
        if filme == 4 and plano_cliente == 'Premium':
            self.lista_filmes.append(input('Qual filme você deseja assistir? '))
            print(f'Ver filme {self.lista_filmes[3]} 1080p HD 4K')
        elif filme == 4 and plano_cliente == 'Basic':
            self.lista_filmes.append(input('Qual filme você deseja assistir? '))
            print(f'Ver filme {self.lista_filmes[3]} 480p Not HD')
        elif filme == 5:
            sleep(1)
            print('\033[31mVolte mais tarde e assista outros filmes!\033[m')
            
    
n = str(input('Digite o seu nome completo: ')).title().strip()
e = str(input('Digite o seu email: ')).strip()
while '@' and '.com' not in e:
    e = str(input('\033[31mDigite seu email novamente:\033[m ')).strip()
print('''[1] Basic
[2] Premium''')
p = int(input('Qual plano você deseja assinar? '))
cliente = Cliente(n, e, p)
sleep(1)
print('\033[33mConfirmando seus dados...\033[m')
sleep(1)
print(f'Nome: {cliente.nome}')
print(f'Email: {cliente.email}')
print(f'Assinante {cliente.plano}')
resp = str(input('Deseja mudar de plano? [S/N] ')).upper()[0].strip()
if resp in 'S':
    sleep(1)
    print('''[1] Basic
[2] Premium''')
    np = int(input('Qual plano você deseja assinar? '))
    cliente.mudar_plano(np)
    print('\033[33mConfirmando seus dados...\033[m')
    sleep(1)
    print(f'Nome: {cliente.nome}')
    print(f'Email: {cliente.email}')
    print(f'Assinante {cliente.plano}')
    print('\033[32mTudo certo! Curta bastante a nossa plataforma!\033[m')
else:
    print('\033[32mTudo Certo! Curta bastante a nossa plataforma!\033[m')
sleep(1)
print('Qual filme você deseja assistir?')
print('''[1] Fast and Furious 9
[2] The Babadook
[3] The Conjuring
[4] Outro
[5] Sair da plataforma''')
f = int(input('----> '))
while f > 5 or f < 1:
    print('\033[31mResposta inválida.\033[m')
    f = int(input('----> '))
cliente.ver_filme(f, cliente.plano)
