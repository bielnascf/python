class Product():
    def __init__(self, product_code, product_description, product_price, discount):
        self.product_code = product_code
        self.product_description = product_description
        self.product_price = product_price
        self.discount = discount
    
    def save(self, prod):
        self.productslist = []
        self.productslist.append(prod)
        print('TABELA PRINCIPAL')
        for pos in range(0, len(products)):
            if pos % 2 == 0:
                print(f'{products[pos]:<30}',end = '')
            else:
                print(f'R${products[pos]:>7.2f}'.replace('.',','))
    
    def changed_list(self, discount):
        print('TABELA ATUALIZADA')
        for pos in range(0, len(products)):
            if pos % 2 == 0:
                print(f'{products[pos]:<30}',end = '')
            else:
                products[pos] = products[pos] - ((products[pos] * discount)/100)
                print(f'R${products[pos]:>7.2f}'.replace('.',','))


def linha():
    print('-=' * 30)

products = []

user_discount = float(input('Qual o percentual de desconto que você deseja aplicar (%)? ')) 
while True:
    linha()
    try:
        user_product_code = int(input('Código do produto: '))
        user_product_description = str(input('Nome do produto: ')).title()
        products.append(user_product_description)
        user_product_price = float(input('Preço do produto: '))
        products.append(user_product_price)
        product = Product(user_product_code, user_product_description, user_product_price, user_discount)
    except:
        print('\033[31mOops... Ocorreu um erro ao digitar uma informação.\033[m')
    else:
        user_answer = str(input('Continuar? [S]/[N] ')).upper()[0].strip()
        if user_answer == 'N':
            break

linha()
product.save(products)
linha()
product.changed_list(user_discount)
linha()