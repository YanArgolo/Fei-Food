# Imports
from random import randint
# O programa deve ser capaz de criar, ler, atualizar e apagar feifood
# Define o menu de opções como um dicionário

menu = {
    1: "Cadastrar novo usuário",
    2: "Login de usuário",
    3: "Buscar por alimento",
    4: "Menu pedidos",
    5: "Menu Admin",
    0: "Sair"
}

# Menu pedidos
menu_pedido = {
    1: "Cadastrar novo pedido",
    2: "Atualizar pedido",
    3: "Excluir pedido",
    4: "Adicionar alimento ao pedido",
    5: "Remover alimento do pedido",
    6: "Avaliar pedido",
    0: "Voltar ao menu principal"
}

menu_admin = {
    1: "login admin",
    2: "Cadastrar alimento",
    3: "Excluir alimento",
    4: "Consultar usuários",
    5: "Total de usuários",
    6: "Quantidade de alimentos",
    7: "Avaliações",
    0: "Voltar ao menu principal"
}

def main():
    """
    Função principal que exibe o menu e chama as funções correspondentes
    de acordo com a escolha do usuário.
    """
    usuario_logado = False
    while True: # Loop infinito
        escolha = exibir_menu() 
        
        if escolha == 1: # Novo contato
            cadastrar_usuario() 
        
        elif escolha == 2: # Procurar contato
            usuario_logado = login() 
        
        elif escolha == 3: # Atualizar contato
            if usuario_logado:
                buscar_alimento() 
            else:
                print("\n# --- ACESSO NEGADO --- #")
                print("Você precisa fazer login para buscar alimentos.")
                print("# --------------------- #\n")
        
        elif escolha == 4: # Menu pedidos
            if usuario_logado:
                while True:
                    escolha_pedido = exibir_menu_pedido()
                    
                    if escolha_pedido == 1:
                        cadastrar_pedido()
                    elif escolha_pedido == 2:
                        editar_pedido()
                    elif escolha_pedido == 3:
                        excluir_pedido()
                    elif escolha_pedido == 4:
                        add_alimento_pedido()
                    elif escolha_pedido == 5:
                        excluir_alimento_pedido()
                    elif escolha_pedido == 6:
                        avaliar_pedido()
                    elif escolha_pedido == 0:
                        break 
                    else:
                        print("Opção inválida. Tente novamente.")
            
            else: 
                print("\n# --- ACESSO NEGADO --- #")
                print("Você precisa fazer login para acessar o menu de pedidos.")
                print("# --------------------- #\n")
                
        elif escolha == 5: # Menu Admin
            
            admin_logado = False
            
            while True:
                escolha_admin = exibir_menu_admin()
                
                if escolha_admin == 1:
            
                    admin_logado = login_adm()
                
                elif escolha_admin == 2:
                    if admin_logado:
                        cadastrar_alimento()
                    else:
                        print("\n# --- ACESSO NEGADO --- #\nVocê precisa fazer login primeiro.\n# --------------------- #\n")
                
                elif escolha_admin == 3:
                    if admin_logado:
                        excluir_alimento()
                    else:
                        print("\n# --- ACESSO NEGADO --- #\nVocê precisa fazer login (Opção 1) primeiro.\n# --------------------- #\n")
                
                elif escolha_admin == 4:
                    if admin_logado:
                        consulta_user()
                    else:
                        print("\n# --- ACESSO NEGADO --- #\nVocê precisa fazer login primeiro.\n# --------------------- #\n")
                
                elif escolha_admin == 5:
                    if admin_logado:
                        total_users()
                    else:
                        print("\n# --- ACESSO NEGADO --- #\nVocê precisa fazer login primeiro.\n# --------------------- #\n")
                
                elif escolha_admin == 6:
                    if admin_logado:
                        total_alimentos()
                    else:
                        print("\n# --- ACESSO NEGADO --- #\nVocê precisa fazer login primeiro.\n# --------------------- #\n")
    
                elif escolha_admin == 7:
                    if admin_logado:
                        estatisticas_pedidos() 
                    else:
                        print("\n# --- ACESSO NEGADO --- #\nVocê precisa fazer login primeiro.\n# --------------------- #\n")   

                elif escolha_admin == 0:
                    break
                else:
                    if escolha_admin != 1:
                        print("Opção inválida. Tente novamente.")
        elif escolha == 0: 
            sair()
        
        else:
            print("Opção inválida. Tente novamente.")
    
# ------------------------------------------ Exibição dos menus ------------------------------------------ #
def exibir_menu():
    """
    Função para exibir o menu de opções e retornar a escolha do usuário.
    :return: Opção escolhida pelo usuário.
    """
    print("Menu:")
    for opcao, descricao in menu.items():
        print(f"{opcao} - {descricao}")
    escolha = int(input("Escolha uma opção: ")) 
    return escolha 

def exibir_menu_pedido():
    """
    Função para exibir o menu de opções e retornar a escolha do usuário.
    :return: Opção escolhida pelo usuário.
    """
    print("Menu Pedidos:")
    for opcao, descricao in menu_pedido.items():
        print(f"{opcao} - {descricao}")
    escolha = int(input("Escolha uma opção: ")) 
    return escolha 

def exibir_menu_admin():
    """
    Função para exibir o menu de opções e retornar a escolha do usuário.
    :return: Opção escolhida pelo usuário.
    """
    print("Menu Admin:")
    for opcao, descricao in menu_admin.items():
        print(f"{opcao} - {descricao}")
    escolha = int(input("Escolha uma opção: ")) 
    return escolha 

# ------------------------------------------ Fim Exibição dos menus ------------------------------------------ #

# ------------------------------------------ Menu Admin ------------------------------------------ #

def login_adm():
    print("# ------------------------------------------------------------------------------------------------- #")
    print("Olá, administrador, faça seu login:")
    nome_login = input("Digite o usuário administrador: ")
    senha_login = input("Digite a senha cadastrada: ")
    print("# ------------------------------------------------------------------------------------------------- #")
    with open("administrador.txt", "r") as arquivo_food:
        conteudo = arquivo_food.readlines() 
 
    for linha in conteudo: 
        nome, senha, = linha.strip().split(",") 
        while True:
            if nome_login.lower()== "sair":
                print("")
                print("Voltando para a pagina anterior...")
                print("")
                return False
            
            if nome_login.lower() == nome.lower() and senha_login == senha: # Verifica se o nome procurado é igual ao nome do contato, ignorando maiúsculas e minúsculas
                print("")
                print("# ---------------------------------------------------------- #")
                print(f"Login bem sucedido! Bem-vindo, Sr.{nome}.")
                print("# ---------------------------------------------------------- #")
                print("") # Imprime os dados do contato encontrado
                 # Sai do loop se o contato for encontrado
                return True
            
            else: # Se não encontrar o contato
                print("Administrador não encontrado, tente novamente.") # Mensagem de erro se o contato não for encontrado
                return False   

#Cadastrar e excluir alimentos do cardápio
def cadastrar_alimento():
    print("# ---------------------------------------------------------- #")
    print("Novo Alimento:")
    nome_alimento = input("Digite o nome do alimento: ")
    quantidade_estoque = input("Digite a quantidade disponivel do alimento: ")
    peso_alimento = input("Digite o peso do alimento: ")
    print("# ---------------------------------------------------------- #")
    #valor_alimento = input("Digite o preço do alimento: R$ ")
    # Abre o arquivo feifood.txt para escrita. Modo "a" para adicionar ao final do arquivo
    arquivo_food = open("alimentos.txt", "a")
    # Grava o contato no arquivo
    arquivo_food.write(f"\n{nome_alimento}, Estoque: {quantidade_estoque} unidades, Peso: {peso_alimento} gramas") # Grava o alimento no arquivo, separando os dados por vírgula
    # Fecha o arquivo
    arquivo_food.close()
    print("# ---------------------------------------------------------- #")
    print("Alimento cadastrado com sucesso!") # Mensagem de sucesso
    print("# ---------------------------------------------------------- #")

def excluir_alimento():
    print("# ---------------------------------------------------------- #")
    alimento_excluir = input("Digite o nome do alimento que deseja excluir: ")
    print("# ---------------------------------------------------------- #")
    # Abre o arquivo alimentos.txt para leitura
    arquivo_food = open("alimentos.txt", "r")
    # Lê o conteúdo do arquivo
    conteudo = arquivo_food.readlines()
    # Fecha o arquivo
    arquivo_food.close()
    # Procura o alimento no arquivo
    for i, linha in enumerate(conteudo):
        if not linha.strip():
            continue  # Pula linhas vazias
        nome_alimento = linha.strip().split(",")
        if alimento_excluir.lower() == nome_alimento[0].lower():
            print("# ---------------------------------------------------------- #")
            print(f"Alimento encontrado: {linha.strip()}")
            # Remove o alimento da lista
            conteudo.pop(i)
            break
    else: # Se não encontrar o alimento
        print("Alimento não encontrado.")
        
    # Abre o arquivo feifood.txt para escrita
    arquivo_food = open("alimentos.txt", "w")
    # Grava os feifood restantes no arquivo
    for linha in conteudo: # Para cada linha no conteúdo do arquivo
        arquivo_food.write(linha) # Grava a linha no arquivo feifood.txt
    # Fecha o arquivo
    arquivo_food.close()
    print("# ---------------------------------------------------------- #")
    print("Alimento excluído com sucesso!") # Mensagem de sucesso
    print("# ---------------------------------------------------------- #")

#Funcao para consultar usuarios existentes
def consulta_user():
    print("# ---------------------------------------------------------- #")
    print("Procurar usuário:")
    user_procurar = input("Digite o nome do usuário que deseja procurar: ")
    print("# ---------------------------------------------------------- #")
    # Abre o arquivo contatos.txt para leitura, lê todo o conteúdo e fecha o arquivo
    with open("feifood.txt", "r") as arquivo_food:
        conteudo = arquivo_food.readlines() # Lê todas as linhas do arquivo e armazena em uma lista
        
    # Procura o contato no arquivo
    for linha in conteudo: # Para cada linha no conteúdo do arquivo
        nome = linha.strip().split(",") # Divide a linha em partes, separando por vírgula
        if user_procurar.lower() == nome[0].lower() and nome[1].lower: # Verifica se o nome procurado é igual ao nome do contato, ignorando maiúsculas e minúsculas
            print("# ---------------------------------------------------------- #")
            print(f"Nome: {nome[0]}, Senha: {nome[1]}")
            print("# ---------------------------------------------------------- #")
            break # Sai do loop se o contato for encontrado
    else: # Se não encontrar o contato
        print("Usuário não encontrado.") # Mensagem de erro se o contato não for encontrado

#def bem_avaliados:

#def mal_avaliados():


#Função para contar o total de usuários cadastrados.
def total_users():
    with open("feifood.txt", "r") as arquivo_food:
        conteudo = arquivo_food.readlines() # Lê todas as linhas do arquivo e armazena em uma lista
    total = len(conteudo) # Conta o número de linhas (usuários)
    print("# ---------------------------------------------------------- #")
    print(f"Total de usuários cadastrados: {total}")
    print("# ---------------------------------------------------------- #")

#Função para contar o total de alimentos cadastrados.
def total_alimentos():
    with open("alimentos.txt", "r") as arquivo_food:
        conteudo = arquivo_food.readlines()
    total = len(conteudo)
    print("# ---------------------------------------------------------- #")
    print(f"Total de alimentos cadastrados: {total-1}")
    print("# ---------------------------------------------------------- #")


def estatisticas_pedidos():
    """
    Função para listar os pedidos mais bem e menos avaliados.
    """
    print("# ---------------------------------------------------------- #")
    print("--- Estatísticas de Avaliações de Pedidos ---")
    
    avaliacoes_por_pedido = {}

    with open("avaliacoes.txt", "r") as arquivo_avaliacao:
        conteudo = arquivo_avaliacao.readlines()

    if not conteudo:
        print("Arquivo de avaliações está vazio. Não há dados para analisar.")
        print("# ---------------------------------------------------------- #")
        return


    for linha in conteudo:
        linha_limpa = linha.strip()
        partes = linha_limpa.split(',')

        codigo_pedido = partes[0].split(':')[-1].strip()
        
        nota_str = partes[1].split(':')[-1].strip()
        
        nota = int(nota_str)
       
        if codigo_pedido not in avaliacoes_por_pedido:
            avaliacoes_por_pedido[codigo_pedido] = [0, 0] # 

        avaliacoes_por_pedido[codigo_pedido][0] += nota
        avaliacoes_por_pedido[codigo_pedido][1] += 1

    if not avaliacoes_por_pedido:
        print("Nenhum pedido válido foi encontrado para análise.")
        print("# ---------------------------------------------------------- #")
        return

    # Calcula a média para cada pedido e armazena em uma lista de tuplas (código, média)
    medias_avaliacoes = []
    for codigo, (soma, contagem) in avaliacoes_por_pedido.items():
        media = soma / contagem
        medias_avaliacoes.append((codigo, media))

    
    medias_avaliacoes.sort(key=lambda x: x[1], reverse=True)

  
    max_nota = medias_avaliacoes[0][1]
    min_nota = medias_avaliacoes[-1][1]
    
    print("# ---------------------------------------------------------- #")
    print("--- Pedidos Mais Bem Avaliados (Nota Máxima) ---")
    for codigo, media in medias_avaliacoes:
        if media == max_nota:
            print(f"Pedido: {codigo}, Média de Avaliação: {media:.2f}")

    print("\n--- Pedidos Menos Avaliados (Nota Mínima) ---")
    for codigo, media in medias_avaliacoes:
        if media == min_nota:
            print(f"Pedido: {codigo}, Média de Avaliação: {media:.2f}")
            
    print("# ---------------------------------------------------------- #")

# ------------------------------------------ Fim menu Admin ------------------------------------------ #


# ------------------------------------------ Menu comum ------------------------------------------ #
def cadastrar_usuario():
    """
    Função para adicionar um novo contato à agenda.
    """
    print("# ---------------------------------------------------------- #")
    print("Novo Usuário:")
    nome = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    print("# ---------------------------------------------------------- #")
    # Abre o arquivo feifood.txt para escrita. Modo "a" para adicionar ao final do arquivo
    arquivo_food = open("feifood.txt", "a")
    # Grava o contato no arquivo
    arquivo_food.write(f"{nome},{senha}\n") # Grava o contato no arquivo, separando os dados por vírgula
    # Fecha o arquivo
    arquivo_food.close()
    print("# ---------------------------------------------------------- #")
    print("Usuário cadastrado com sucesso!") # Mensagem de sucesso
    print("# ---------------------------------------------------------- #")
    
def login():
    """
    Procurar um contato na agenda pelo nome.
    Se o contato for encontrado, imprime os dados do contato.
    Se não for encontrado, imprime uma mensagem de erro.
    :return: None
    """
    print("# ---------------------------------------------------------- #")
    print("Faça login:")
    nome_login = input("Digite o usuário cadastrado: ")
    senha_login = input("Digite a senha cadastrada: ")
    print("# ---------------------------------------------------------- #")
    
    with open("feifood.txt", "r") as arquivo_food:
        conteudo = arquivo_food.readlines() 
        
    
    for linha in conteudo: 
        dados = linha.strip().split(",") 

        if len(dados) != 2:
            continue

        nome, senha = dados[0], dados[1] 
        
        if nome_login.lower() == "sair":
            print("")
            print("Voltando para a pagina anterior...")
            print("")
            return False
            
        if nome_login.lower() == nome.lower() and senha_login == senha: 
            print("")
            print("# ---------------------------------------------------------- #")
            print(f"Login bem sucedido! Bem-vindo, {nome}.")
            print("") 
            return True 
            
    print("# ---------------------------------------------------------- #")
    print("Usuário não encontrado, tente novamente.") 
    return False

def buscar_alimento():
    print("# ---------------------------------------------------------- #")
    print("Buscar alimento:")
    alimento_src = input("Digite o nome do alimento que deseja procurar: ")
    print("# ---------------------------------------------------------- #")
    with open("alimentos.txt", "r") as arquivo_food:
        conteudo = arquivo_food.readlines() 
        
    for linha in conteudo: 
        alimentos = linha.strip().split(",") 
        if alimento_src.lower() == alimentos[0].lower()and alimentos[1].lower() and alimentos[2].lower(): 
            print("")
            print("# ---------------------------------------------------------- #")
            print(f"Alimento disponível! Faça seu pedido.")
            print(alimentos[0], alimentos[1] , alimentos[2])
            print("")
            break 

    else: 
        print("# ---------------------------------------------------------- #")
        print("Alimento indisponível, escolha outra opção.") 
# ------------------------------------------ Fim menu ------------------------------------------ #


# ------------------------------------------------------ Menu pedido --------------------------------------------------- #
def cadastrar_pedido():
    """
    Função para cadastrar um novo pedido, listando os alimentos para escolha
    """
    print("# ---------------------------------------------------------- #")
    print("\n---Cadastrar Novo Pedido ---")
    print("# ---------------------------------------------------------- #")
    
    # Lista o alimento pra pessoa escolher
    alimentos_disponiveis = []
   
    with open("alimentos.txt", "r") as arquivo_food:
        # Filtra linhas vazias e armazena em uma lista
        alimentos_disponiveis = [linha.strip() for linha in arquivo_food if linha.strip()]
            
    if  (alimentos_disponiveis == " "):
        print("# ---------------------------------------------------------- #")
        print(" O cardápio está vazio. Não é possível fazer um pedido.")
        return

    print("# ---------------------------------------------------------- #")
    print("--- \nCardápio de Alimentos Disponíveis: ---")
    print("# ---------------------------------------------------------- #")
    for i, linha in enumerate(alimentos_disponiveis, 1):
        print(f"{i} - {linha}")
        print()
    # Abre o pedidos.txt para cadastrar o pedido
    arquivo_food = open("pedidos.txt", "a")
    # Coleta e valida a escolha
  
    escolha = input("Digite o **número** do alimento que deseja pedir (ou '0' para cancelar): ")
    if escolha == '0':
        print("Cadastro de pedido cancelado.")
        return

    indice_escolhido = int(escolha) - 1

    if 0 <= indice_escolhido < len(alimentos_disponiveis):
        pedido = alimentos_disponiveis[indice_escolhido].split(",")[0].strip()
    else:
        print("Opção inválida. Digite um número válido da lista.")
   
    tipo = input("Digite o tipo do pedido (Entrega ou Retirada): ").strip().lower()
    codigo_pedido = randint(1000, 9999) 
    telefone = input("Telefone para contato: ")
    
    if tipo == "entrega":
        endereco = input("Digite seu endereço completo: ")
        arquivo_food.write(f"{codigo_pedido}, {pedido}, Entrega, {endereco}, {telefone}\n" )
        mensagem_sucesso = (f"Pedido de Entrega {codigo_pedido} cadastrado com sucesso!")

    elif tipo == "retirada":
        arquivo_food.write (f" {codigo_pedido}, {pedido}, Retirada, FEI, {telefone}\n")
        mensagem_sucesso = (f"Pedido de Retirada {codigo_pedido} cadastrado com sucesso!")

    else:
        print("---------------------")
        print(f"Tipo de pedido '{tipo}' inválido.")
        print("---------------------")
        return
      
    print("---------------------")
    print(mensagem_sucesso)
    print("---------------------")
    arquivo_food.close()   

def editar_pedido():
    """
    Atualiza os dados de um contato existente na agenda.
    :return: None
    """
    print("# ---------------------------------------------------------- #")
    print("Editar pedido:")
    pedido_editar = input("Digite o código do pedido que deseja editar: ")
    print("# ---------------------------------------------------------- #")
    
    # Abre o arquivo feifood.txt para leitura
    arquivo_food = open("pedidos.txt", "r")
    conteudo = arquivo_food.readlines()
    arquivo_food.close()

    for i, linha in enumerate(conteudo): # Para cada indice e linha no conteúdo do arquivo 
        
       
        if not linha.strip():
            continue 
            
        codigo_pedido, pedido, tipo, endereco, telefone = linha.strip().split(",") 
        

        if pedido_editar.lower() == codigo_pedido.strip().lower():
            print(f"Pedido encontrado: {linha.strip()}") 
            
            print(codigo_pedido.strip()) 
            novo_pedido= input("Digite o novo pedido que deseja fazer (deixe em branco para não alterar): ")
            novo_tipo = input("Entrega ou retirada? (deixe em branco para não alterar): ")
            novo_endereco = input("Digite o novo endereço (deixe em branco para não alterar): ")
            novo_telefone = input("Digite o novo telefone (deixe em branco para não alterar): ")
            pedido_antigo = pedido.strip()
            tipo_antigo = tipo.strip()
            endereco_antigo = endereco.strip()
            telefone_antigo = telefone.strip()

            if novo_pedido == "0" or novo_pedido == "":
                novo_pedido = pedido_antigo

            if novo_tipo == "0" or novo_tipo == "":
                novo_tipo = tipo_antigo

            if novo_endereco == "0" or novo_endereco == "":
                novo_endereco = endereco_antigo

            if novo_telefone == "0" or novo_telefone == "":
                 novo_telefone = telefone_antigo

            conteudo[i] = f"{codigo_pedido.strip()},{novo_pedido},{novo_tipo},{novo_endereco},{novo_telefone}\n"

            arquivo_food = open("pedidos.txt", "w")
            # Grava os feifood atualizados no arquivo
            for linha_salvar in conteudo: 
                arquivo_food.write(linha_salvar) 
            # Fecha o arquivo
            arquivo_food.close()
            print("# ---------------------------------------------------------- #")
            print("Pedido atualizado com sucesso!") 
            print("# ---------------------------------------------------------- #")

            break 
    
    else: 
        print("# ---------------------------------------------------------- #")
        print("Pedido não encontrado.") 
        

def excluir_pedido():
    print("# ---------------------------------------------------------- #")
    pedido_excluir = input("Digite o código do pedido que deseja excluir: ")
    # Abre o arquivo alimentos.txt para leitura
    arquivo_food = open("pedidos.txt", "r")
    # Lê o conteúdo do arquivo
    conteudo = arquivo_food.readlines()
    # Fecha o arquivo
    arquivo_food.close()
    # Procura o alimento no arquivo
    for i, linha in enumerate(conteudo):
        if not linha.strip():
            continue  # Pula linhas vazias
        cod_pedido = linha.strip().split(",")
        if pedido_excluir.lower() == cod_pedido[0].lower():
            print(f"Pedido encontrado: {linha.strip()}")
            # Remove o alimento da lista
            conteudo.pop(i)
            
             # Abre o arquivo feifood.txt para escrita
            arquivo_food = open("pedidos.txt", "w")
            # Grava os feifood restantes no arquivo
            for linha in conteudo: # Para cada linha no conteúdo do arquivo
                arquivo_food.write(linha) # Grava a linha no arquivo feifood.txt
            # Fecha o arquivo
            arquivo_food.close()
            print("# ---------------------------------------------------------- #")
            print("Pedido excluído com sucesso!") # Mensagem de sucesso
            
            break
    else: # Se não encontrar o alimento
        print("Pedido não encontrado.")

def add_alimento_pedido():
    print("# ---------------------------------------------------------- #")
    print("Adicionar alimento ao pedido: ")
    pedido_adicionar = input("Digite o código do pedido que deseja adicionar alimento: ")
    
    # Abre o arquivo feifood.txt para leitura
    arquivo_food = open("pedidos.txt", "r")
    conteudo = arquivo_food.readlines()
    arquivo_food.close()
    
    for i, linha in enumerate(conteudo): # Para cada indice e linha no conteúdo do arquivo 
        
        if not linha.strip():
            continue
            
        codigo_pedido, pedido, tipo, endereco, telefone = linha.strip().split(",") 
        
    
        if pedido_adicionar.lower() == codigo_pedido.strip().lower():
            print("# ---------------------------------------------------------- #")
            print(f"Pedido encontrado: {linha.strip()}") 
            print("# ---------------------------------------------------------- #")
            # Atualiza os dados do contato
            print("# ---------------------------------------------------------- #")
            print("--- \nCardápio de Alimentos Disponíveis: ---")
            print("# ---------------------------------------------------------- #")
            
            with open("alimentos.txt", "r") as arquivo_food_cardapio: # Renomeei a variável
                alimentos_disponiveis = []
                alimentos_disponiveis = [linha_cardapio.strip() for linha_cardapio in arquivo_food_cardapio if linha_cardapio.strip()]

                if not alimentos_disponiveis:
                    print("O cardápio está vazio. Não é possível fazer um pedido.")
                    return
                        
            for c, linha_cardapio in enumerate(alimentos_disponiveis, 1):
                print(f"{c} - {linha_cardapio}")
                print()

            print("# ---------------------------------------------------------- #")
            novo_alimento= input("Digite o novo alimento que deseja adicionar ao pedido: ")

            alimento_valido = False
            for item_do_cardapio in alimentos_disponiveis:
                if novo_alimento.lower() in item_do_cardapio.lower():
                    alimento_valido = True
                    break

            if not alimento_valido:
                print(f"{novo_alimento} não faz parte do cardápio.")
                return 

            conteudo[i] = f"{codigo_pedido.strip()},{pedido.strip()} + {novo_alimento},{tipo.strip()},{endereco.strip()},{telefone.strip()}\n"

            # Abre o arquivo pedidos.txt para escrita
            arquivo_food = open("pedidos.txt", "w")
            # Grava os feifood atualizados no arquivo
            for linha_salvar in conteudo:
                arquivo_food.write(linha_salvar) 
            # Fecha o arquivo
            arquivo_food.close()
            print("# ---------------------------------------------------------- #")
            print("Alimento adicionado ao pedido com sucesso!") # Mensagem de sucesso
            print("# ---------------------------------------------------------- #")

            break 
    
    else: # Se não encontrar o pedido
        print("# ---------------------------------------------------------- #")
        print("Pedido não encontrado.") 
        print("# ---------------------------------------------------------- #")

def excluir_alimento_pedido():
    print("# ---------------------------------------------------------- #")
    print("Remover alimento do pedido: ")
    pedido_remover = input("Digite o código do pedido que deseja remover alimento: ")
    print("# ---------------------------------------------------------- #")
    
    # Abre o arquivo feifood.txt para leitura
    arquivo_food = open("pedidos.txt", "r")
    conteudo = arquivo_food.readlines()
    arquivo_food.close()
    
    # Procura o contato no arquivo
    for i, linha in enumerate(conteudo): # Para cada indice e linha no conteúdo do arquivo 
        
        if not linha.strip():
            continue
            
        codigo_pedido, pedido, tipo, endereco, telefone = linha.strip().split(",") 
        
        if pedido_remover.lower() == codigo_pedido.strip().lower():
            print("# ---------------------------------------------------------- #")
            print(f"Pedido encontrado: {linha.strip()}") 
            
            alimento_remover = input("Digite o alimento que deseja remover do pedido: ")

            novos_itens = pedido.strip().replace(f" + {alimento_remover}", "").replace(f"{alimento_remover} + ", "").replace(alimento_remover, "")

            conteudo[i] = f"{codigo_pedido.strip()},{novos_itens.strip()},{tipo.strip()},{endereco.strip()},{telefone.strip()}\n"

            # Abre o arquivo pedidos.txt para escrita
            arquivo_food = open("pedidos.txt", "w")
            # Grava os feifood atualizados no arquivo
            for linha_salvar in conteudo: 
                arquivo_food.write(linha_salvar) 
            # Fecha o arquivo
            arquivo_food.close()
            print("Alimento removido do pedido com sucesso!")
            print("# ---------------------------------------------------------- #") 

            break 
    
    else: # Se não encontrar o pedido
        print("# ---------------------------------------------------------- #")
        print("Pedido não encontrado.") 
        print("# ---------------------------------------------------------- #")

def avaliar_pedido():
   # Lista os pedidos existentes
    pedidos_feitos = []
    
    # Abre o arquivo 'pedidos.txt' para ler a lista de pedidos a serem exibidos
    with open("pedidos.txt", "r") as arquivo_food:
        # Lê o conteúdo para a lista pedidos_feitos
        pedidos_feitos = [linha.strip() for linha in arquivo_food if linha.strip()]
    
    if not pedidos_feitos:
        print("# ---------------------------------------------------------- #")
        print("Não existe nenhum pedido para avaliar.")
        return

    print("--- \nPedidos para Avaliação: ---")
    for i, linha in enumerate(pedidos_feitos, 1):
        print(f"{i} - {linha}")
        print()
    print("# ---------------------------------------------------------- #")
    pedido_avaliar = input("Digite o código do pedido que deseja avaliar: ").strip()
    
    with open("pedidos.txt", "r") as arquivo_food:
        conteudo = arquivo_food.readlines()

    encontrado = False
    
    # Procura o pedido pelo código
    for linha in conteudo: 
        partes = linha.strip().split(",") 
        codigo_pedido = partes[0].strip()
            
        if pedido_avaliar.lower() == codigo_pedido.lower():
            print(f"\nPedido encontrado: {linha.strip()}")
            encontrado = True
            
            while True:
                print("# ---------------------------------------------------------- #")
                nota_str = input("Digite um número inteiro de 0 a 5 para avaliar com estrelas o pedido: ").strip()
                nota = int(nota_str)
                if 0 <= nota <= 5:
                    break
                else:
                    print("Nota inválida. Digite um número entre 0 e 5.") 
            
            # Grava a avaliação no arquivo 'avaliacoes.txt'
            with open("avaliacoes.txt", "a") as arquivo_avaliacao:
                arquivo_avaliacao.write(f"Pedido: {codigo_pedido}, Avaliação: {nota}\n")
            
            print(f"Pedido {codigo_pedido} avaliado com sucesso! Nota registrada: {nota}")
            break 
            
    if not encontrado:
        print("# ---------------------------------------------------------- #")
        print("Pedido não encontrado. Verifique o código e tente novamente.")
    
# ------------------------------------------ Fim menu pedido ------------------------------------------ #

# ------------------------------------------ Inicia o programa ------------------------------------------ #
def sair():
    """
    Função para sair do programa.
    :return: None
    """
    print("Saindo...")
    exit() # Encerra o programa
            
if __name__ == "__main__":
    main() # Chama a função main para iniciar o programa