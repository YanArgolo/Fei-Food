# Imports
from random import randint
# O programa deve ser capaz de criar, ler, atualizar e apagar feifood
# Define o menu de opções como um dicionário
menu = {
    1: "Cadastrar novo usuário",
    2: "Login de usuário",
    3: "Buscar por alimento",
    4: "Pesquisar Alimento",
    5: "Cadastrar alimento", #ADM TESTE
    6: "Excluir alimento", #ADM TESTE
    7: "Login de administrador", #ADM TESTE
    8: "Consultar Usuários", #ADM TESTE
    9: "Total de usuarios cadastrados", #ADM TESTE
    10: "Quantidade de Alimentos cadastrados", #ADM TESTE#
    11: "Menu pedidos",
    0: "Sair"
}

# Menu pedidos
menu_pedido = {
    1: "Cadastrar novo pedido",
    2: "Atualizar pedido",
    3: "Alterar alimento",
    4: "Adicionar alimento ao pedido",
    5: "Excluir pedido",
    0: "Voltar ao menu principal"
}

def main():
    """
    Função principal que exibe o menu e chama as funções correspondentes
    de acordo com a escolha do usuário.
    """
    while True: # Loop infinito
        escolha = exibir_menu() # Chama a função exibir_menu e armazena a escolha do usuário
        if escolha == 1: # Novo contato
            cadastrar_usuario() # Chama a função novo_contato
        elif escolha == 2: # Procurar contato
            login() # Chama a função procurar_contato
        elif escolha == 3: # Atualizar contato
            buscar_alimento() # Chama a função atualizar_contato
        elif escolha == 4: # Apagar contato
            apagar_contato() # Chama a função apagar_contato
        elif escolha == 5: # Cadastrar alimento Teste
            cadastrar_alimento()
        elif escolha == 6: # Excluir alimento Teste
            excluir_alimento()
        elif escolha == 7: # Login ADM Teste
            login_adm()
        elif escolha == 8: # Login ADM Teste
            consulta_user()
        elif escolha == 9:
            total_users()
        elif escolha == 10:
            total_alimentos()
        elif escolha == 11:

            #Laco para exibir menu pedido
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
                    print
                elif escolha_pedido == 0:
                    print("Voltando ao menu principal...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        elif escolha == 0: # Sair
            sair() # Chama a função sair
        else:
            print("Opção inválida. Tente novamente.") # Mensagem de erro para opção inválida
    

def exibir_menu():
    """
    Função para exibir o menu de opções e retornar a escolha do usuário.
    :return: Opção escolhida pelo usuário.
    """
    print("Menu:")
    for opcao, descricao in menu.items():
        print(f"{opcao} - {descricao}")
    escolha = int(input("Escolha uma opção: ")) # Lê a opção escolhida pelo usuário, sem validar
    return escolha # Retorna a opção escolhida

def exibir_menu_pedido():
    """
    Função para exibir o menu de opções e retornar a escolha do usuário.
    :return: Opção escolhida pelo usuário.
    """
    print("Menu Pedidos:")
    for opcao, descricao in menu_pedido.items():
        print(f"{opcao} - {descricao}")
    escolha = int(input("Escolha uma opção: ")) # Lê a opção escolhida pelo usuário, sem validar
    return escolha # Retorna a opção escolhida

#Funcionalidades do ADM
###

def login_adm():
    print("Olá, administrador, faça seu login:")
    nome_login = input("Digite o usuário administrador: ")
    senha_login = input("Digite a senha cadastrada: ")
    # Abre o arquivo feifood.txt para leitura, lê todo o conteúdo e fecha o arquivo
    with open("administrador.txt", "r") as arquivo_food:
        conteudo = arquivo_food.readlines() # Lê todas as linhas do arquivo e armazena em uma lista
        
    # Procura o contato no arquivo
    for linha in conteudo: # Para cada linha no conteúdo do arquivo
        nome, senha, = linha.strip().split(",") # Divide a linha em partes, separando por vírgula
        while True:
            if nome_login.lower()== "sair":
                print("")
                print("Voltando para a pagina anterior...")
                print("")
                return False
            
            if nome_login.lower() == nome.lower() and senha_login == senha: # Verifica se o nome procurado é igual ao nome do contato, ignorando maiúsculas e minúsculas
                print("")
                print(f"Login bem sucedido! Bem-vindo, Sr.{nome}.")
                print("") # Imprime os dados do contato encontrado
                 # Sai do loop se o contato for encontrado
                return True
            
            else: # Se não encontrar o contato
                print("Administrador não encontrado, tente novamente.") # Mensagem de erro se o contato não for encontrado
                return False   

#Cadastrar e excluir alimentos do cardápio
def cadastrar_alimento():
    print("Novo Alimento:")
    nome_alimento = input("Digite o nome do alimento: ")
    quantidade_estoque = input("Digite a quantidade disponivel do alimento: ")
    peso_alimento = input("Digite o peso do alimento: ")
    #valor_alimento = input("Digite o preço do alimento: R$ ")
    # Abre o arquivo feifood.txt para escrita. Modo "a" para adicionar ao final do arquivo
    arquivo_food = open("alimentos.txt", "a")
    # Grava o contato no arquivo
    arquivo_food.write(f"\n{nome_alimento}, Estoque: {quantidade_estoque} unidades, Peso: {peso_alimento} gramas") # Grava o alimento no arquivo, separando os dados por vírgula
    # Fecha o arquivo
    arquivo_food.close()
    print("Alimento cadastrado com sucesso!") # Mensagem de sucesso

def excluir_alimento():
    alimento_excluir = input("Digite o nome do alimento que deseja excluir: ")
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
    print("Alimento excluído com sucesso!") # Mensagem de sucesso

#Funcao para consultar usuarios existentes
def consulta_user():
    print("Procurar usuário:")
    user_procurar = input("Digite o nome do usuário que deseja procurar: ")
    # Abre o arquivo contatos.txt para leitura, lê todo o conteúdo e fecha o arquivo
    with open("feifood.txt", "r") as arquivo_food:
        conteudo = arquivo_food.readlines() # Lê todas as linhas do arquivo e armazena em uma lista
        
    # Procura o contato no arquivo
    for linha in conteudo: # Para cada linha no conteúdo do arquivo
        nome = linha.strip().split(",") # Divide a linha em partes, separando por vírgula
        if user_procurar.lower() == nome[0].lower() and nome[1].lower: # Verifica se o nome procurado é igual ao nome do contato, ignorando maiúsculas e minúsculas
            print(f"Nome: {nome[0]}, Senha: {nome[1]}")
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
    print(f"Total de usuários cadastrados: {total}")

#Função para contar o total de alimentos cadastrados.
def total_alimentos():
    with open("alimentos.txt", "r") as arquivo_food:
        conteudo = arquivo_food.readlines()
    total = len(conteudo)
    print(f"Total de alimentos cadastrados: {total}")


#Funcionalidades do usuario comum
def cadastrar_usuario():
    """
    Função para adicionar um novo contato à agenda.
    """
    print("Novo Usuário:")
    nome = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    # Abre o arquivo feifood.txt para escrita. Modo "a" para adicionar ao final do arquivo
    arquivo_food = open("feifood.txt", "a")
    # Grava o contato no arquivo
    arquivo_food.write(f"{nome},{senha}\n") # Grava o contato no arquivo, separando os dados por vírgula
    # Fecha o arquivo
    arquivo_food.close()
    print("Usuário cadastrado com sucesso!") # Mensagem de sucesso
    
def login():
    """
    Procurar um contato na agenda pelo nome.
    Se o contato for encontrado, imprime os dados do contato.
    Se não for encontrado, imprime uma mensagem de erro.
    :return: None
    """
    print("Faça login:")
    nome_login = input("Digite o usuário cadastrado: ")
    senha_login = input("Digite a senha cadastrada: ")
    # Abre o arquivo feifood.txt para leitura, lê todo o conteúdo e fecha o arquivo
    with open("feifood.txt", "r") as arquivo_food:
        conteudo = arquivo_food.readlines() # Lê todas as linhas do arquivo e armazena em uma lista
        
    # Procura o contato no arquivo
    for linha in conteudo: # Para cada linha no conteúdo do arquivo
        nome, senha, = linha.strip().split(",") # Divide a linha em partes, separando por vírgula
        while True:
            if nome_login.lower()== "sair":
                print("")
                print("Voltando para a pagina anterior...")
                print("")
                return False
            
            if nome_login.lower() == nome.lower() and senha_login == senha: # Verifica se o nome procurado é igual ao nome do contato, ignorando maiúsculas e minúsculas
                print("")
                print(f"Login bem sucedido! Bem-vindo, {nome}.")
                print("") # Imprime os dados do contato encontrado
                 # Sai do loop se o contato for encontrado
                return True
            
            else: # Se não encontrar o contato
                print("Usuário não encontrado, tente novamente.") # Mensagem de erro se o contato não for encontrado
                return False   

def buscar_alimento():
    print("Buscar alimento:")
    alimento_src = input("Digite o nome do alimento que deseja procurar: ")
    # Abre o arquivo contatos.txt para leitura, lê todo o conteúdo e fecha o arquivo
    with open("alimentos.txt", "r") as arquivo_food:
        conteudo = arquivo_food.readlines() # Lê todas as linhas do arquivo e armazena em uma lista
        
    # Procura o contato no arquivo
    for linha in conteudo: # Para cada linha no conteúdo do arquivo
        alimentos = linha.strip().split(",") # Divide a linha em partes, separando por vírgula
        if alimento_src.lower() == alimentos[0].lower()and alimentos[1].lower() and alimentos[2].lower(): # Verifica se o nome procurado é igual ao nome do contato, ignorando maiúsculas e minúsculas
            print("")
            print(f"Alimento disponível! Faça seu pedido.")
            print(alimentos[0], alimentos[1] , alimentos[2])
            print("")
            break # Sai do loop se o contato for encontrado

    else: # Se não encontrar o contato
        print("Alimento indisponível, escolha outra opção.") # Mensagem de erro se o alimento não estiver disponivel


# Menu pedido
def cadastrar_pedido():
    """
    Função para cadastrar um novo pedido, listando os alimentos para escolha
    """
    print("\n---Cadastrar Novo Pedido ---")
    
    # Lista o alimento pra pessoa escolher
    alimentos_disponiveis = []
   
    with open("alimentos.txt", "r") as arquivo_food:
        # Filtra linhas vazias e armazena em uma lista
        alimentos_disponiveis = [linha.strip() for linha in arquivo_food if linha.strip()]
            
    if  (alimentos_disponiveis == " "):
        print(" O cardápio está vazio. Não é possível fazer um pedido.")
        return

    print("--- \nCardápio de Alimentos Disponíveis: ---")
    for i, linha in enumerate(alimentos_disponiveis, 1):
        # Exibe apenas a primeira parte da linha (o nome do alimento) para simplificar a escolha
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

# funcao para editar pedidos existentes
def editar_pedido():
    """
    Atualiza os dados de um contato existente na agenda.
    :return: None
    """
    print("Editar pedido:")
    pedido_editar = input("Digite o código do pedido que deseja editar: ")
    # Abre o arquivo feifood.txt para leitura
    arquivo_food = open("pedidos.txt", "r")
    # Lê o conteúdo do arquivo
    conteudo = arquivo_food.readlines()
    # Fecha o arquivo
    arquivo_food.close()
    # Procura o contato no arquivo
    for i, linha in enumerate(conteudo): # Para cada indice e linha no conteúdo do arquivo 
        codigo_pedido, pedido, tipo, endereco, telefone = linha.strip().split(",") # Divide a linha em partes, separando por vírgula
        if pedido_editar.lower() == codigo_pedido.lower():# Verifica se o nome procurado é igual ao nome do contato, ignorando maiúsculas e minúsculas
            print(f"Pedido encontrado: {linha.strip()}") # Imprime os dados do contato encontrado
            # Atualiza os dados do contato
            print(codigo_pedido)
            novo_pedido= input("Digite o novo pedido que deseja fazer (deixe em branco para não alterar): ")
            novo_tipo = input("Entrega ou retirada? (deixe em branco para não alterar): ")
            novo_endereco = input("Digite o novo endereço (deixe em branco para não alterar): ")
            novo_telefone = input("Digite o novo telefone (deixe em branco para não alterar): ")

            # Retorna aos valores preenchidos anteriormente se o usuário deixar em branco
            novo_pedido = novo_pedido or pedido
            novo_tipo = novo_tipo or tipo
            novo_endereco = novo_endereco or endereco
            novo_telefone = novo_telefone or telefone

            #atualiza a linha específica no conteúdo
            conteudo[i] = f"{codigo_pedido},{novo_pedido},{novo_tipo},{novo_endereco}, {novo_telefone}\n"

            # Abre o arquivo pedidos.txt para escrita
            arquivo_food = open("pedidos.txt", "w")
            # Grava os feifood atualizados no arquivo
            for linha in conteudo: # Para cada linha no conteúdo do arquivo
                arquivo_food.write(linha) # Grava a linha no arquivo feifood.txt
            # Fecha o arquivo
            arquivo_food.close()
            print("Pedido atualizado com sucesso!") # Mensagem de sucesso

        break # Sai do loop se o contato for encontrado
    else: # Se não encontrar o pedido
        print("Pedido não encontrado.") # Mensagem de erro se o contato não for encontrado
        
#Funcao para excluir pedidos existentes
def excluir_pedido():
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
            print("Pedido excluído com sucesso!") # Mensagem de sucesso
            
            break
    else: # Se não encontrar o alimento
        print("Pedido não encontrado.")

# Excluir pedido
# def excluir_pedido():
#     cd_pedido_excluir = input("Digite o código do pedido que deseja excluir: ")


#     # Abre o arquivo pedidos.txt para leitura
#     with open("pedidos.txt", "r") as arquivo_food:
#             # Lê o conteúdo do arquivo
#             conteudo = arquivo_food.readlines()

#     # Lista para armazenar as linhas que NÃO serão excluídas
#     novo_conteudo = []
#     excluido = False
    

#     # Procura o pedido no arquivo
#     for linha in conteudo:
#         linha_limpa = linha.strip()
#         if not linha_limpa:
#             continue  # Pula linhas vazias
            
#         # 1. Encontra a parte que contém o código
#         if "Código:" in linha_limpa:
#             # Pega o primeiro segmento (ex: "Código: 1234")
#             primeira_parte = linha_limpa.split(",")[0].strip()
            
#             # 2. Extrai SOMENTE o número do código 
#             try:
#                 codigo_na_linha = primeira_parte.split(":")[1].strip()
#             except IndexError:
#                 # Caso a linha não esteja no formato esperado (ex: falta ":")
#                 codigo_na_linha = "" 

#             # 3. Compara o código digitado com o código extraído da linha
#             if cd_pedido_excluir == codigo_na_linha:
#                 print(f"Pedido encontrado e excluído: {linha_limpa}")
#                 excluido = True
#                 # Nao adiciona esta linha ao novo_conteudo (a exclusão acontece aqui)
#             else:
#                 novo_conteudo.append(linha) # Mantém a linha
#         else:
#             # Mantém linhas que não parecem ser um registro de pedido
#             novo_conteudo.append(linha) 

#     # Se não encontrar o pedido
#     if not excluido: 
#         print("Pedido não encontrado.")
#         return

#     # Abre o arquivo pedidos.txt para escrita (sobrescreve)
#     with open("pedidos.txt", "w") as arquivo_food:
#         # Grava os pedidos restantes no arquivo
#         arquivo_food.writelines(novo_conteudo)

#     print("Pedido excluído com sucesso!")

#Função para adicionar alimento a um pedido existente
def add_alimento_pedido():
    print("Adicionar alimento ao pedido:")
    pedido_adicionar = input("Digite o código do pedido que deseja adicionar alimento: ")
    # Abre o arquivo feifood.txt para leitura
    arquivo_food = open("pedidos.txt", "r")
    # Lê o conteúdo do arquivo
    conteudo = arquivo_food.readlines()
    # Fecha o arquivo
    arquivo_food.close()
    # Procura o contato no arquivo
    for i, linha in enumerate(conteudo): # Para cada indice e linha no conteúdo do arquivo 
        codigo_pedido, pedido, tipo, endereco, telefone = linha.strip().split(",") # Divide a linha em partes, separando por vírgula
        if pedido_adicionar.lower() == codigo_pedido.lower():# Verifica se o nome procurado é igual ao nome do contato, ignorando maiúsculas e minúsculas
            print(f"Pedido encontrado: {linha.strip()}") # Imprime os dados do contato encontrado
            # Atualiza os dados do contato
            novo_alimento= input("Digite o novo alimento que deseja adicionar ao pedido: ")

            #atualiza a linha específica no conteúdo
            conteudo[i] = f"{codigo_pedido},{pedido} + {novo_alimento},{tipo},{endereco}, {telefone}\n"

            # Abre o arquivo pedidos.txt para escrita
            arquivo_food = open("pedidos.txt", "w")
            # Grava os feifood atualizados no arquivo
            for linha in conteudo: # Para cada linha no conteúdo do arquivo
                arquivo_food.write(linha) # Grava a linha no arquivo feifood.txt
            # Fecha o arquivo
            arquivo_food.close()
            print("Alimento adicionado ao pedido com sucesso!") # Mensagem de sucesso

        break # Sai do loop se o contato for encontrado
    else: # Se não encontrar o pedido
        print("Pedido não encontrado.") # Mensagem de erro se o contato não for encontrado


def atualizar_contato():
    """
    Atualiza os dados de um contato existente na agenda.
    :return: None
    """
    print("Atualizar contato:")
    nome_atualizar = input("Digite o nome do contato que deseja atualizar: ")
    # Abre o arquivo feifood.txt para leitura
    arquivo_food = open("feifood.txt", "r")
    # Lê o conteúdo do arquivo
    conteudo = arquivo_food.readlines()
    # Fecha o arquivo
    arquivo_food.close()
    # Procura o contato no arquivo
    for i, linha in enumerate(conteudo): # Para cada indice e linha no conteúdo do arquivo 
        nome, sobrenome, telefone, email = linha.strip().split(",") # Divide a linha em partes, separando por vírgula
        if nome_atualizar.lower() == nome.lower(): # Verifica se o nome procurado é igual ao nome do contato, ignorando maiúsculas e minúsculas
            print(f"Contato encontrado: {linha.strip()}") # Imprime os dados do contato encontrado
            # Atualiza os dados do contato
            novo_nome = input("Digite o novo nome (deixe em branco para não alterar): ")
            novo_sobrenome = input("Digite o novo sobrenome (deixe em branco para não alterar): ")
            novo_telefone = input("Digite o novo telefone (deixe em branco para não alterar): ")
            novo_email = input("Digite o novo e-mail (deixe em branco para não alterar): ")
            # Atualiza os dados do contato, se o usuário não deixar o nome em branco
            if novo_nome:
                conteudo[i] = f"{novo_nome},{novo_sobrenome},{novo_telefone},{novo_email}\n"
            else:
                conteudo[i] = f"{nome},{sobrenome},{telefone},{email}\n"
            break # Sai do loop se o contato for encontrado
    else: # Se não encontrar o contato
        print("Contato não encontrado.") # Mensagem de erro se o contato não for encontrado
        
    # Abre o arquivo feifood.txt para escrita
    arquivo_food = open("feifood.txt", "w")
    # Grava os feifood atualizados no arquivo
    for linha in conteudo: # Para cada linha no conteúdo do arquivo
        arquivo_food.write(linha) # Grava a linha no arquivo feifood.txt
    # Fecha o arquivo
    arquivo_food.close()
    print("Contato atualizado com sucesso!") # Mensagem de sucesso
    
def apagar_contato():
    """
    Apaga um contato da agenda.
    :return: None
    """
    nome_apagar = input("Digite o nome do contato que deseja apagar: ")
    # Abre o arquivo feifood.txt para leitura
    arquivo_food = open("feifood.txt", "r")
    # Lê o conteúdo do arquivo
    conteudo = arquivo_food.readlines()
    # Fecha o arquivo
    arquivo_food.close()
    # Procura o contato no arquivo
    for i, linha in enumerate(conteudo):
        nome, sobrenome, telefone, email = linha.strip().split(",")
        if nome_apagar.lower() == nome.lower():
            print(f"Contato encontrado: {linha.strip()}")
            # Remove o contato da lista
            conteudo.pop(i)
            break
    else: # Se não encontrar o contato
        print("Contato não encontrado.")
        
    # Abre o arquivo feifood.txt para escrita
    arquivo_food = open("feifood.txt", "w")
    # Grava os feifood restantes no arquivo
    for linha in conteudo: # Para cada linha no conteúdo do arquivo
        arquivo_food.write(linha) # Grava a linha no arquivo feifood.txt
    # Fecha o arquivo
    arquivo_food.close()
    print("Contato apagado com sucesso!") # Mensagem de sucesso
    
def sair():
    """
    Função para sair do programa.
    :return: None
    """
    print("Saindo...")
    exit() # Encerra o programa
            
if __name__ == "__main__":
    main() # Chama a função main para iniciar o programa