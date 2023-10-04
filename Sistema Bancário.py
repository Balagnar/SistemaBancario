 #Codigo criado para o desafio DIO do curso Formação Python Dev

#Desenvolvido por: Angelo Gabriel Nunes Pinheiro da Silva

#Desafio de Projeto: Desenvolver um sistema bancario com saque, deposito e extrado

#____________________________________________________________________________________________________________________________________________

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
=>"""

saldo = 0
limite = 500
numero_saques = 0
list_extrato = []
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
        
    elif opcao == "3":
        print("Extrato")
        for transacao in list_extrato:
            print(transacao)
        
        
    elif opcao == 4:                #If de inicio da função Sair
        print("Sair")
        break
    
