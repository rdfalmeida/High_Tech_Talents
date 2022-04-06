# Global variables:

#global 'opcao' in def main_menu
global lista
lista = []

#Local variables:
# 'usuario' in def welcome
# 'nome', 'data_nasc', 'endereco' in def cadastrar

# Printing welcome user message:
def welcome():
	usuario = input("Entre com o seu nome: ")
	if usuario == "":
		print("Seja Bem-vindo(a), usuário!\n")
	else:
		print(f"Seja Bem-vindo(a), {usuario}!\n")

#This is for invalid option:
def try_again():
	print("Opção Inválida! Tente novamente.")

#This is for exiting the program:			
def exit_program():
	print("Saindo do sistema...")

# Starting inital screen after getting user name, with validation loop:
def main_menu():
	global opcao
	while True:
		try:
			opcao = int(input("Selecione uma opção:\n1 - Cadastrar\n2 - Listar\n3 - Sair\n"))
		except ValueError:
			try_again()
			continue
		if not opcao in [1,2,3]:
			try_again()
			continue
		if opcao == 1:
			cadastrar()
		elif opcao == 2:
			listar()
		elif opcao == 3:
			exit_program()
			break
				
# This is to register someone in the database:
def cadastrar():
	nome = ""
	while nome == "":
		nome = input("Coloque o nome: ")
	data_nasc = ""
	while data_nasc == "":
		data_nasc = input("Coloque a data de nascimento: ")		
	endereco = ""
	while endereco == "":
		endereco = input("Coloque o endereço: ")

	registro = {"Nome":nome, "Data_Nascimento":data_nasc, "Endereco": endereco}
	lista.append(registro)
	print("Sucesso! Cadastrado!")

#To list registered entries:
def listar():
	for item in lista:
		print(item)

#Below is the main program:
welcome()
main_menu()