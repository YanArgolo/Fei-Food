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
    10: "Quantidade de Alimentos cadastrados", #ADM TESTE
    0: "Sair"
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