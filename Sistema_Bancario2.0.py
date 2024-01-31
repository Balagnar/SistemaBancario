import random

print("Selecione uma das opções")

menu = '''

[1] Novo Acesso
[2] Deposito
[3] Saque 
[4] Extrato
[5] Sair
=> '''

dados_user = [{'nome', 'idade', 'cpf'}]
cod_unico = []
extratos = []

saldo = 0
num_Saque = 0
limite = 500
transacao = 0


def func_menu():
    while True:
        
        opcao = input(menu)
    
        if opcao == "1":

                def criar_conta():
                    print("Criação de Conta\n")  
                    print("Informe seu dados a baixo")
                    idade = int(input("Idade: "))
                    if idade >= 18:
                        nome = input("Nome e SobreNome: ")
                        cpf = input("Cpf: ")
                        
                        dados_user.append({'nome':nome, 'idade':idade, 'cpf':cpf})
                        
                        num = random.randint(1, 100) #gera um numero aleatorio de 1 a 100
                        cod_unico.append({num}) #armazena o numero aleatorio na lista cod_unico
                        
                criar_conta()      
                
        elif opcao == "2":
            
            def deposito():
                
                global saldo, transacao
                
                print("Deposito\n")
                print("Seu saldo atual é de: ", saldo, "R$.\n")
                deposito = int(input("Informe o valor do deposito: "))
                ("Confirma deposito de: ", deposito, "R$ ?.\n")
                sn = input("[S/N]? \n")
                if sn == "s":
                    saldo = deposito + saldo
                    print("Seu saldo atual é de: ", saldo, "R$")
                else:
                    deposito = input("Informe o valor correto: \n")
                    saldo = deposito + saldo
                    print("Seu saldo atual é de: ", saldo, "R$")
                    
                    transacao = "depositado {}".format(saldo)
                
            deposito()    
        
        elif opcao == "3":
            
            def saque():
                
                global saldo, num_Saque, transacao
                
                if num_Saque < 3:
                    
                    print("Saque \n")
                    print("Seu saldo atual é de: ", saldo, "R$.\n")
                    saque = int(input("Informe o valor do extrato: "))
                    ("Confirma extrato de: ", saque, "R$ ?.\n")
                    sn = input("[S/N]? \n")
                    if sn == "s":
                        if saque <= saldo:
                            saldo = saldo - saque
                            print("Seu saldo atual é de: ", saldo, "R$")
                            
                            num_Saque = num_Saque + 1
                            
                            transacao = "sacado {}".format(saldo)
                    else:
                        print("Transação Cancelada")
                        
                            
                else:
                    print("Quantidade de Saques Excedido")            
                            
            saque()
    
        elif opcao == "4":
            
            def extrato():
            
                print("Extrato\n")
            for transacao in extratos:
                print(transacao)
            
            extrato()    
                    
        elif opcao == "5":
            
            def sair():
            
                print("Até a proxima.")
                break
            
            sair()                                   
func_menu()