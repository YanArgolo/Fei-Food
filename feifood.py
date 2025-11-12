# Exercício 04
# Crie uma agenda de telefones que salva os dados de maneira
# permanente.
# A agenda deve funcionar em loop infinito, até que o usuário
# decida sair. Os dados armazenados são: nome, sobrenome,
# telefone e e-mail.
# A agenda deve apresentar o seguinte menu para o usuário:
# ▶ 1- Novo contato (create)
# ▶ 2- Procura (pelo nome) (read)
# ▶ 3- Atualiza contato (update)
# ▶ 4- Apaga contato (delete)
# ▶ 0- Sair

# O programa deve ser capaz de criar, ler, atualizar e apagar feifood
from random import randint
# Define o menu de opções como um dicionário
menu = {
    1: "Cadastrar novo usuário",
    2: "Login de usuário",
    3: "Buscar por alimento",
    4: "Pesquisar Alimento",
    5: "Cadastrar alimento", #ADM TESTE
    6: "     alimento", #ADM TESTE
    7: "Menu pedidos",
    0: "Sair"
}

# Menu para as ações do pedido
menu_pedido = {
    1: "Cadastrar novo pedido",
    2: "Atualizar pedido",
    3: "Alterar ou Remover alimento",
    4: "Excluir pedido",
    0: "Sair"
}

def main():
    """
    Função principal que exibe o menu e chama as funções correspondentes
    de acordo com a escolha do usuário.
    """
    
    while True:  # Loop infinito
        escolha = exibir_menu()  # Chama a função exibir_menu e armazena a escolha do usuário

        if escolha == 1:  # Cadastrar novo usuário
            cadastrar_usuario()

        elif escolha == 2:  # Login
            login()

        elif escolha == 3:  # Buscar alimento
            buscar_alimento()

        elif escolha == 4:  # Apagar contato
            apagar_contato()

        elif escolha == 5:  # Cadastrar alimento (Admin)
            cadastrar_alimento()

        elif escolha == 6:  # Excluir alimento (Admin)
            excluir_alimento()

        elif escolha == 7:  # Menu de pedidos
            while True:
                escolha_pedido = exibir_menu_pedido()

                if escolha_pedido == 1:
                    cadastrar_pedido()
                elif escolha_pedido == 2:
                    atualizar_pedido()
                elif escolha_pedido == 3:
                    print("Função alterar/remover alimento ainda não implementada.")
                elif escolha_pedido == 4:
                    print("Função excluir pedido ainda não implementada.")
                elif escolha_pedido == 0:
                    print("Voltando ao menu principal...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif escolha == 0:  # Sair do programa
            sair()

        else:
            print("Opção inválida. Tente novamente.")


    
   
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
    print("Menu dos pedidos:")
    for opcao, descricao in menu_pedido.items():
        print(f"{opcao} - {descricao}")
    escolha = int(input("Escolha uma opção: ")) # Lê a opção escolhida pelo usuário, sem validar
    return escolha # Retorna a opção escolhida

#Funcionalidades do ADM
###

#Cadastrar e excluir alimentos do cardápio
def cadastrar_alimento():
    print("Novo Alimento:")
    nome_alimento = input("Digite o nome do alimento: ")
    #valor_alimento = input("Digite o preço do alimento: R$ ")
    # Abre o arquivo feifood.txt para escrita. Modo "a" para adicionar ao final do arquivo
    arquivo_food = open("alimentos.txt", "a")
    # Grava o contato no arquivo
    arquivo_food.write(f"{nome_alimento}\n") # Grava o alimento no arquivo, separando os dados por vírgula
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
        if alimento_excluir == nome_alimento:
            print(f"Alimento encontrado: {linha.strip()}")
            # Remove o alimento da lista
            conteudo.pop(i)
            break
    else: # Se não encontrar o alimento
        print("Alimento não encontrado.")
        
    # Abre o arquivo feifood.txt para escrita
    arquivo_food = open("feifood.txt", "w")
    # Grava os feifood restantes no arquivo
    for linha in conteudo: # Para cada linha no conteúdo do arquivo
        arquivo_food.write(linha) # Grava a linha no arquivo feifood.txt
    # Fecha o arquivo
    arquivo_food.close()
    print("Alimento excluído com sucesso!") # Mensagem de sucesso


def cadastrar_pedido():
    arquivo_food = open("pedidos.txt", "a")
    # Grava o contato no arquivo
    print("Novo Pedido:")
    local_pedido = input("Digite o local do pedido: ")
    tipo = input("Digite o tipo do pedido se é Entrega ou Retirada: ")
    codigo_pedido = randint(1,9999)
    if tipo == "Entrega" or tipo=="entrega":
        endereco = input("Digite seu endereço: ")
        telefone = float(input("Telefone para contato:"))
        pedido = input("Digite o pedido: ")
        arquivo_food.write(f"Código do pedido: {codigo_pedido} Pedido: {pedido} Local do pedido: {local_pedido} Tipo de entrega: {tipo} Endereço usuário {endereco} Telefone para contato: {telefone}\n") # Grava o alimento no arquivo, separando os dados por vírgula
        print("---------------------")
        print("Pedido cadastrado com sucesso!")
        print("---------------------") # Mensagem de sucesso
    elif tipo == "Retirada" or tipo=="retirada":
        telefone = float(input("Telefone para contato:"))
        pedido = input("Digite o pedido: ")
        arquivo_food.write(f"Código do pedido: {codigo_pedido} Pedido: {pedido} Local do pedido: {local_pedido} Tipo de entrega: {tipo} Telefone para contato: {telefone}\n") # Grava o alimento no arquivo, separando os dados por vírgula
        print("---------------------")
        print("Pedido cadastrado com sucesso!")
        print("---------------------") # Mensagem de sucesso
    else:
        print("---------------------")
        print("Erro ao cadastrar pedido!")
        print("---------------------")
    arquivo_food.close()



def cadastrar_usuario():
    """
    Função para cadastrar um novo usuário
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
    with open("feifood.txt", "r") as arquivo_food:
        conteudo = arquivo_food.readlines() # Lê todas as linhas do arquivo e armazena em uma lista
        
    # Procura o contato no arquivo
    for linha in conteudo: # Para cada linha no conteúdo do arquivo
        alimentos = linha.strip().split(",") # Divide a linha em partes, separando por vírgula
        if alimento_src.lower() == alimentos.lower(): # Verifica se o nome procurado é igual ao nome do contato, ignorando maiúsculas e minúsculas
            print(f"Alimento disponível: {alimento_src}, Preço: {preco}")
            break # Sai do loop se o contato for encontrado
    else: # Se não encontrar o contato
        print("Contato não encontrado.") # Mensagem de erro se o contato não for encontrado

def atualizar_pedido():
    """
    Atualiza os dados de um contato existente na agenda.
    :return: None
    """
    print("Atualizar pedido:")
    codigo_pedido = input("Digite o código do pedido que deseja atualizar: ")
    # Abre o arquivo feifood.txt para leitura
    arquivo_food = open("pedidos.txt", "r")
    # Lê o conteúdo do arquivo
    conteudo = arquivo_food.readlines()
    # Fecha o arquivo
    arquivo_food.close()
    # Procura o pedido no arquivo
    for i, linha in enumerate(conteudo): # Para cada indice e linha no conteúdo do arquivo 
        codigo,tipo, endereco, telefone, pedido = linha.strip().split(",") # Divide a linha em partes, separando por vírgula
        if codigo_pedido.lower() == codigo.lower(): # Verifica se o nome procurado é igual ao nome do contato, ignorando maiúsculas e minúsculas
            print(f"Contato encontrado: {linha.strip()}") # Imprime os dados do contato encontrado
            # Atualiza os dados do contato
            novo_tipo = input("Digite o novo tipo se é Entrega ou Retirada (deixe em branco para não alterar): ")
            novo_pedido = input("Digite o novo pedido (deixe em branco para não alterar): ")
            novo_telefone = input("Digite o novo telefone (deixe em branco para não alterar): ")
            novo_endereco = input("Digite o novo endereço (deixe em branco para não alterar): ")
            # Atualiza os dados do contato, se o usuário não deixar o nome em branco
            if codigo_pedido:
                conteudo[i] = f"{codigo},{novo_tipo},{novo_pedido},{novo_telefone},{novo_endereco}\n"
            else:
                conteudo[i] = f"{codigo},{tipo},{endereco},{telefone},{pedido}\n"
            break # Sai do loop se o contato for encontrado
    else: # Se não encontrar o contato
        print("Código não encontrado.") # Mensagem de erro se o contato não for encontrado
        
    # Abre o arquivo feifood.txt para escrita
    arquivo_food = open("pedidos.txt", "w")
    # Grava os feifood atualizados no arquivo
    for linha in conteudo: # Para cada linha no conteúdo do arquivo
        arquivo_food.write(linha) # Grava a linha no arquivo feifood.txt
    # Fecha o arquivo
    arquivo_food.close()
    print("---------------------")
    print("Pedido atualizado com sucesso!") # Mensagem de sucesso
    print("---------------------")
    
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