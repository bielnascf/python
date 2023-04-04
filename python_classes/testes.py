# EXEMPLO PRÁTICO
class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

    # MÉTODOS DO CONTROLE (FUNÇOES -> DEFs)
    def passar_canal(self, botao):
        if botao == '+':
            print('Aumentar Canal')
        elif botao == '-':
            print('Diminuir Canal')


controle_remoto = ControleRemoto('preto', '10 cm', '2 cm', '2 cm')
print(controle_remoto.cor)
print(controle_remoto.passar_canal('+'))

controle_remoto2 = ControleRemoto('cinza', '8 cm', '2 cm', '2 cm')
print(controle_remoto2.cor)
print(controle_remoto2.passar_canal('-'))
