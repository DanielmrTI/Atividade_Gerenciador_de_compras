usuarios = []
produtos = []
historico_compras = []
admin_login = 'admin'
admin_senha = '123456'

def exibir_catalogo():
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for produto in produtos:
            print(f"{produto['nome']} - R${produto['preco']} - {produto['descricao']} - Estoque: {produto['quantidade']}")

def adicionar_produto_carrinho(usuario_atual):
    print("\n Adicionar Produtos ao Carrinho")
    if not produtos:
        print("Não há produtos disponíveis para adicionar ao carrinho.")
        return

    exibir_catalogo()
    nome_produto = input("Digite o nome do produto que deseja adicionar ao carrinho: ")
    
    produto_encontrado = False
    for produto in produtos:
        if produto['nome'] == nome_produto:
            quantidade_desejada = int(input(f"Quantidade desejada de {produto['nome']}: "))
            if quantidade_desejada > produto['quantidade']:
                print("Quantidade indisponível no estoque.")
            else:
                produto_encontrado = True
            
                if 'carrinho' not in usuario_atual:
                    usuario_atual['carrinho'] = []
                usuario_atual['carrinho'].append({
                    'nome': produto['nome'],
                    'preco': produto['preco'],
                    'quantidade': quantidade_desejada
                })
                produto['quantidade'] -= quantidade_desejada
                print(f"{quantidade_desejada} unidades de {produto['nome']} adicionadas ao carrinho.")
                break
    
    if not produto_encontrado:
        print("Produto não encontrado.")

def remover_produto_carrinho(usuario_atual):
    print("\n Remover Produtos do Carrinho")
    if 'carrinho' not in usuario_atual or not usuario_atual['carrinho']:
        print("Carrinho vazio.")
        return

    print("Produtos no Carrinho:")
    for i, item in enumerate(usuario_atual['carrinho'], start=1):
        print(f"{i}. {item['nome']} - Quantidade: {item['quantidade']}")

    try:
        opcao = int(input("Escolha o número do produto que deseja remover: ")) - 1
        if 0 <= opcao < len(usuario_atual['carrinho']):
            produto_removido = usuario_atual['carrinho'].pop(opcao)
        
            for produto in produtos:
                if produto['nome'] == produto_removido['nome']:
                    produto['quantidade'] += produto_removido['quantidade']
                    print(f"{produto_removido['quantidade']} unidades de {produto_removido['nome']} removidas do carrinho.")
                    break
        else:
            print("Opção inválida.")
    except ValueError:
        print("Opção inválida.")

def visualizar_carrinho(usuario_atual):
    print("\n Visualização de Carrinho")
    if 'carrinho' not in usuario_atual or not usuario_atual['carrinho']:
        print("Carrinho vazio.")
    else:
        print("Produtos no Carrinho:")
        for item in usuario_atual['carrinho']:
            print(f"{item['nome']} - Quantidade: {item['quantidade']}")

def processo_compra(usuario_atual):
    print("\n Processo de Compra")
    if 'carrinho' not in usuario_atual or not usuario_atual['carrinho']:
        print("Carrinho vazio. Adicione produtos ao carrinho primeiro.")
        return

    total_compra = 0
    print("Produtos no Carrinho:")
    for item in usuario_atual['carrinho']:
        subtotal = item['quantidade'] * item['preco']
        print(f"{item['nome']} - Quantidade: {item['quantidade']} - Subtotal: R${subtotal}")
        total_compra += subtotal

 
    print(f"Total da compra: R${total_compra}")
    opcao = input("Deseja confirmar a compra? (s/n): ").lower()
    if opcao == 's':
      
        historico_compras.append({
            'usuario': usuario_atual['nome'],
            'itens_comprados': usuario_atual['carrinho'],
            'total': total_compra
        })
      
        usuario_atual['carrinho'] = []
        print("Compra realizada com sucesso!")
    else:
        print("Compra cancelada.")

def exibir_historico_compras():
    print("\n Histórico de Compras")
    if not historico_compras:
        print("Nenhuma compra realizada ainda.")
    else:
        for compra in historico_compras:
            print(f"Usuário: {compra['usuario']}")
            print("Itens comprados:")
            for item in compra['itens_comprados']:
                print(f"{item['nome']} - Quantidade: {item['quantidade']} - Preço unitário: R${item['preco']}")
            print(f"Total da compra: R${compra['total']}")
            print("-" * 30)

def adicionar_produto_estoque():
    print("\n Adicionar Produto ao Estoque")
    nome_produto = input("Nome do Produto: ")
    preco_produto = float(input("Preço do Produto: "))
    descricao_produto = input("Descrição do Produto: ")
    quantidade_produto = int(input("Quantidade em Estoque: "))
    produtos.append({
        'nome': nome_produto,
        'preco': preco_produto,
        'descricao': descricao_produto,
        'quantidade': quantidade_produto
    })
    print("Produto adicionado ao estoque!")

while True:
    print("\n Gerenciador de Compras")
    print("1. Cadastro de Usuário")
    print("2. Login de Usuário")
    print("3. Login de Administrador")
    print("4. Adicionar Produtos ao Estoque")
    print("5. Catálogo de Produtos")
    print("6. Adicionar Produtos ao Carrinho")
    print("7. Remover Produtos do Carrinho")
    print("8. Visualização de Carrinho")
    print("9. Processo de Compra")
    print("10. Histórico de Compras")
    print("0. Sair do Sistema")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        print("\n Cadastro de Usuário")
        nome = input("Nome: ")
        email = input("E-mail: ")
        senha = input("Senha: ")
        usuarios.append({'nome': nome, 'email': email, 'senha': senha})
        print("Usuário cadastrado com sucesso!")

    elif opcao == '2':
        print("\n Login de Usuário")
        email = input("E-mail: ")
        senha = input("Senha: ")
        usuario_atual = None
        for usuario in usuarios:
            if usuario['email'] == email and usuario['senha'] == senha:
                usuario_atual = usuario
                print("Login realizado com sucesso!")
                break
        else:
            print("Usuário não encontrado. Tente novamente.")

    elif opcao == '3':
        print("\n Login de Administrador")
        login = input("Login de Administrador: ")
        senha = input("Senha de Administrador: ")
        if login == admin_login and senha == admin_senha:
            print("Login de administrador realizado com sucesso!")
            usuario_atual = {'nome': 'Admin'}
        else:
            print("Credenciais de administrador inválidas.")
            usuario_atual = None

    elif opcao == '4':
        if usuario_atual and 'nome' in usuario_atual and usuario_atual['nome'] == 'Admin':
            adicionar_produto_estoque()
        else:
            print("Acesso negado. Faça login como administrador.")

    elif opcao == '5':
        print("\n Catálogo de Produtos")
        exibir_catalogo()

    elif opcao == '6':
        if usuario_atual:
            adicionar_produto_carrinho(usuario_atual)
        else:
            print("Faça login primeiro.")

    elif opcao == '7':
        if usuario_atual:
            remover_produto_carrinho(usuario_atual)
        else:
            print("Faça login primeiro.")

    elif opcao == '8':
        if usuario_atual:
            visualizar_carrinho(usuario_atual)
        else:
            print("Faça login primeiro.")

    elif opcao == '9':
        if usuario_atual:
            processo_compra(usuario_atual)
        else:
            print("Faça login primeiro.")

    elif opcao == '10':
        if usuario_atual:
            exibir_historico_compras()
        else:
            print("Faça login primeiro.")

    elif opcao == '0':
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida")