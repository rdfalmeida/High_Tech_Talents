# Variables:

    # global 'usuario' defined in def welcome
    # global 'opcao' defined in def initial_screen

# Printing welcome user message:
def welcome():
	global usuario
	usuario = input("Entre com o seu nome: ")
	print(f"Seja Bem-vindo {usuario}!\n")

# Starting inital screen after getting user name:
def initial_screen():
	global opcao
	print("Selecione uma opção:")
	print("1 - Multiplicar")
	print("2 - Sair")
	opcao = int(input(""))

# This function uses 'opcao' value to direct what is to be done: multiplying, exit program, or invalid option 
def switch():
	while True:
		if opcao in [1,2]:
			if opcao == 1: #Multiplicar
				multiplying()
				break
			elif opcao == 2:#Sair
				exit_program()
				break
		else:
		   try_again()

#This is for printing the multiplication table from 0 to 10:
def multiplying():
	print("Iniciando a multiplicação")
	for i in range(11):
		for j in range(11):
			print(f"{i} x {j} = {i*j}")
		print("\n")
	print("Sucesso!")

#This is for exiting the program:			
def exit_program():
	print("Saindo do sistema...")

#This is for invalid option
def try_again():
	print("Opção Inválida! Tente novamente.")
	initial_screen()
	
#Below is the main program:

welcome()
initial_screen()
switch()