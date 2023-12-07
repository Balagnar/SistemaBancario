#Codigo criado para o desafio DIO do curso Formação Python Dev

#Desenvolvido por: Angelo Gabriel Nunes Pinheiro da Silva

#Desafio de Projeto: Desenvolver um sistema bancario com saque, deposito e extrado. v1.0
#Desafio de Projeto: Aprimorar o sistema criado. v2.0

#____________________________________________________________________________________________________________________________________________

#----------COMO CRIAR UMA LISTA DE DICIONARIOS COM CHAVES ESPECIFICAS EM PYTHON---------------------------#

"""
# Criando uma lista de dicionários
minha_lista = [{'nome': 'João', 'idade': 30}, {'nome': 'Maria', 'idade': 25}]

# Adicionando um dicionário à lista
minha_lista.append({'nome': 'Carlos', 'idade': 35})

# Imprimindo a lista
for item in minha_lista:
    print(item)

{'nome': 'João', 'idade': 30}
{'nome': 'Maria', 'idade': 25}
{'nome': 'Carlos', 'idade': 35}

"""

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Criar_Usuario
[5] Criar_Conta_Corrente
[6] Sair
=>"""

saldo = 0
limite = 500
numero_saques = 0
list_extrato = []
lista_user = [{'nome', 'idade', 'cpf', 'senha'}]
transacao = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "1":                #If de inicio da função Deposito
        print("Deposito\n")
        print("Seu saldo atual é de: ",(saldo),"R$\n")
        deposito = input("Informe o valor do deposito: ")
        deposito = float(deposito)
        if deposito >= 0:
            saldo = (saldo + deposito)
            print ("Deposito efetuado com sucesso!")
            print("Seu saldo atual é de: ", saldo, "R$\n")
            transacao = "depositado {}".format(saldo)
            list_extrato.append(transacao)
        else:
            print("Deposito não pode ser 0")   
        
    elif opcao == "2":              #Ilif de inicio da função Sacar
        print("Sacar\n")
        print("Você tem direito a 3 saques por dia.")
        print("Você efetuou:" , numero_saques, "saques.")
        if numero_saques < LIMITE_SAQUES:
            print("Seu saldo atual é de: ",(saldo),"R$\n")
            saque = input("Informe o valor do saque: ")
            saque = float(saque)
            if saque >= 0 and saque <= saldo and saque <= limite:
                saldo = (saldo - saque)
                print ("Saque efetuado com sucesso!")
                print("Seu saldo atual é de: ", saldo, "R$\n")
                numero_saques = (numero_saques + 1)
                transacao = "sacado {}".format(saldo)
                list_extrato.append(transacao)
        else:
            print("Você atingiu seu limite de saques no dia")
        
    elif opcao == "3":              #Ilif de inicio da função Extrato         
        print("Extrato\n") 
        for transacao in list_extrato:
            print(transacao)
        
        
    elif opcao == "4":              #Ilif de inicio da função Criar_Usuario
        print("Criar Usuario\n")
        print("Bem-vindo a criação de usuários\n")
        print("Vamos dar inicio a criação do seu login\n")
        nome = input("Informe seu nome:")
        idade = input("Informe a sua idade:")
        cpf = input("informe seu cpf:")
        c_senha = input("crie uma senha de 4 digitos:")     
        lista_user.append({'nome':nome, 'idade':idade, 'cpf':cpf, 'senha':c_senha})
        
    elif opcao == "5":              #Ilif de inicio da função Criar_Conta_Corrente
        print("Criar Conta Corrente\n")
        print("Se já possui usuario, continue nessa tela, se não, selecione a opção para criar usuario")
        login = input("Informe seu nome:")
        if login == nome:
           l_senha = input("Informe sua senha:")
           if l_senha == c_senha:
               print("Sua conta é 0001") 
        
    elif opcao == "6":                #If de inicio da função Sair
        print("Sair")
        break
    