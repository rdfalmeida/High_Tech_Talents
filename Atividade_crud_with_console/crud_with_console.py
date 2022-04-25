# Global variables:
list_cliente = []
list_contrato = []
list_imovel = []

#-------------MAIN MENU
# Starting inital screen after getting user name, with validation loop:
def main_menu():
	while True:
		opcao = int(input("Selecione uma opção:\n1 - Cadastrar\n2 - Listar\n3 - Deletar\n4 - Gerar Contrato com dados cadastrados\n5 - Sair\n"))
		if not opcao in [1,2,3,4,5]:
			try_again()
		if opcao == 1:
			cadastrar_menu()
		elif opcao == 2:
			listar_menu()
		elif opcao == 3:
			delete_menu()
		elif opcao == 4:
			gerar_contrato()
		elif opcao == 5:
			exit_program()

#-------------CADASTRAR MODULE

# Cadastar Module main page.
# More categories, fields and parameters can be added as necessary.
def cadastrar_menu():
		opcao = int(input("O que deseja cadastar?\n1 - Cliente\n2 - Contrato\n3 - Imóvel\n4 - Voltar\n5 - Sair\n"))
		if not opcao in [1,2,3,4,5]:
			try_again()
		if opcao == 1:
			cadastrar_cliente()
		elif opcao == 2:
			cadastrar_contrato()
		elif opcao == 3:
			cadastrar_imovel()
		elif opcao == 4:
			main_menu()
		elif opcao == 5:
			exit_program()

# Add Cliente
def cadastrar_cliente():
	nome = ""
	documento = ""

	while nome == "":
		nome = input("Informe o nome: ")		
	while documento == "":
		documento = input("Informe o documento: ")
	registro_cliente = {"Nome":nome, "Documento":documento}
	list_cliente.append(registro_cliente)
	print("Sucesso! Cadastrado!")

# Add Contrato
def cadastrar_contrato():
	locador = ""
	locatario = ""
	imovel_objeto = ""
	termos = ""

	while locador == "":
		locador = input("Informe o ID do locador: ")		
	while locatario == "":
		locatario = input("Informe o locatário: ")
	while imovel_objeto == "":
		imovel_objeto = input("Informe o ID imóvel a ser alugado: ")
	while termos == "":
		termos = input("Informe os termos do contrato: ")
	registro_contrato = {"Locador":locador, "Locatario":locatario, "Imóvel Objeto":imovel_objeto, "Termos":termos}
	list_contrato.append(registro_contrato)
	print("Sucesso! Cadastrado!")

# Add Imóvel
def cadastrar_imovel():
	matricula = ""
	endereco = ""

	while matricula == "":
		matricula = input("Informe a matrícula: ")		
	while endereco == "":
		endereco = input("Informe o endereço: ")
	registro_imovel = {"Matrícula":matricula, "Endereco":endereco}
	list_imovel.append(registro_imovel)
	print("Sucesso! Cadastrado!")

#-------------LISTAR MODULE

# Listar Module main page
def listar_menu():
		opcao = int(input("O que deseja listar?:\n1 - Clientes\n2 - Contratos\n3 - Imóveis\n4 - Todas as categorias\n5 - Voltar\n6 - Sair\n"))
		if not opcao in [1,2,3,4,5,6]:
			try_again()
		if opcao == 1:
			listar_menu_cliente()
		elif opcao == 2:
			listar_menu_contrato()
		elif opcao == 3:
			listar_menu_imovel()
		elif opcao == 4:
			listar_all_categories()
		elif opcao == 5:
			main_menu()
		elif opcao == 6:
			exit_program()

# Listar Cliente view submenu
def listar_menu_cliente():
		opcao = int(input("Como deseja listar?:\n1 - Selecionar por ID\n2 - Todos os clientes\n3 - Voltar\n4 - Sair\n"))
		if not opcao in [1,2,3,4]:
			try_again()
		if opcao == 1:
			listar_byid_cliente()
		elif opcao == 2:
			listar_all_cliente()
		elif opcao == 3:
			listar_menu()
		elif opcao == 4:
			exit_program()

# Listar Contrato view submenu
def listar_menu_contrato():
		opcao = int(input("Como deseja listar?:\n1 - Selecionar por ID\n2 - Todos os contratos\n3 - Voltar\n4 - Sair\n"))
		if not opcao in [1,2,3,4]:
			try_again()
		if opcao == 1:
			listar_byid_contrato()
		elif opcao == 2:
			listar_all_contrato()
		elif opcao == 3:
			listar_menu()
		elif opcao == 4:
			exit_program()

# Listar Imóvel view submenu
def listar_menu_imovel():
		opcao = int(input("Como deseja listar?:\n1 - Selecionar por ID\n2 - Todos os imóveis\n3 - Voltar\n4 - Sair\n"))
		if not opcao in [1,2,3,4]:
			try_again()
		if opcao == 1:
			listar_byid_imovel()
		elif opcao == 2:
			listar_all_imovel()
		elif opcao == 3:
			listar_menu()
		elif opcao == 4:
			exit_program()

# Show all items from all categories
def listar_all_categories():
	print("Lista de clientes: ")
	listar_all_cliente()
	print("Lista de contratos: ")
	listar_all_contrato()
	print("Lista de imóveis: ")
	listar_all_imovel()

# Show Cliente by ID
def listar_byid_cliente():
	if len(list_cliente) == 0:
		is_empty()
	else:
		listar_all_cliente()
		id = int(input('Informe o ID do cliente a ser visualizado: '))
		i = id - 1
		print("ID = ",id ,"\n", list_cliente[i],"\n")

# Show Contrato by ID
def listar_byid_contrato():
	if len(list_contrato) == 0:
		is_empty()
	else:
		listar_all_contrato()
		id = int(input('Informe o ID do contrato a ser visualizado: '))
		i = id - 1
		print("ID = ",id ,"\n", list_contrato[i],"\n")

# Show Imóvel by ID
def listar_byid_imovel():
	if len(list_imovel) == 0:
		is_empty()
	else:
		listar_all_imovel()
		id = int(input('Informe o ID do imóvel a ser visualizado: '))
		i = id - 1
		print("ID = ",id ,"\n", list_imovel[i],"\n")

# Show All Clientes
def listar_all_cliente():
	if len(list_cliente) == 0:
		is_empty()
	i = 0
	while (i < len(list_cliente)):
		id = i + 1
		print("ID = ",id ,"\n", list_cliente[i],"\n")
		i += 1

# Show All Contratos
def listar_all_contrato():
	if len(list_contrato) == 0:
		is_empty()
	i = 0
	while (i < len(list_contrato)):
		id = i + 1
		print("ID = ",id ,"\n", list_contrato[i],"\n")
		i += 1

# Show All Imóveis
def listar_all_imovel():
	if len(list_imovel) == 0:
		is_empty()
	i = 0
	while (i < len(list_imovel)):
		id = i + 1
		print("ID = ",id ,"\n", list_imovel[i],"\n")
		i += 1

#-------------DELETAR MODULE

# Deletar Module main page
def delete_menu():
		opcao = int(input("O que deseja deletar?:\n1 - Clientes\n2 - Contratos\n3 - Imóveis\n4 - Todas as categorias\n5 - Voltar\n6 - Sair\n"))
		if not opcao in [1,2,3,4,5,6]:
			try_again()
		if opcao == 1:
			delete_menu_cliente()
		elif opcao == 2:
			delete_menu_contrato()
		elif opcao == 3:
			delete_menu_imovel()
		elif opcao == 4:
			delete_all_categories()
		elif opcao == 5:
			main_menu()
		elif opcao == 6:
			exit_program()

# Cliente view submenu
def delete_menu_cliente():
		opcao = int(input("Como deseja deletar?:\n1 - Selecionar por ID\n2 - Todos os clientes\n3 - Voltar\n4 - Sair\n"))
		if not opcao in [1,2,3,4]:
			try_again()
		if opcao == 1:
			delete_byid_cliente()
		elif opcao == 2:
			delete_all_cliente()
		elif opcao == 3:
			delete_menu()
		elif opcao == 4:
			exit_program()

# Delete Contrato view submenu
def delete_menu_contrato():
		opcao = int(input("Como deseja deletar?:\n1 - Selecionar por ID\n2 - Todos os contratos\n3 - Voltar\n4 - Sair\n"))
		if not opcao in [1,2,3,4]:
			try_again()
		if opcao == 1:
			delete_byid_contrato()
		elif opcao == 2:
			delete_all_contrato()
		elif opcao == 3:
			delete_menu()
		elif opcao == 4:
			exit_program()

# Delete Imóvel submenu
def delete_menu_imovel():
		opcao = int(input("Como deseja deletar?:\n1 - Selecionar por ID\n2 - Todos os imóveis\n3 - Voltar\n4 - Sair\n"))
		if not opcao in [1,2,3,4]:
			try_again()
		if opcao == 1:
			delete_byid_imovel()
		elif opcao == 2:
			delete_all_imovel()
		elif opcao == 3:
			listar_menu()
		elif opcao == 4:
			exit_program()

# Delete items from all categories
def delete_all_categories():
	delete_all_cliente()
	delete_all_contrato()
	delete_all_imovel()

# Delete Cliente by ID
def delete_byid_cliente():
	if len(list_cliente) == 0:
		is_empty()
	else:
		listar_all_cliente()
		id = int(input('Informe o ID do cliente a ser deletado: '))
		i = id - 1
		print("ID = ",id ,"\n", list_cliente[i],"\n")
		list_cliente.pop(i)
		print("Cliente deletado!")

# Delete Contrato by ID
def delete_byid_contrato():
	if len(list_contrato) == 0:
		is_empty()
	else:
		listar_all_contrato()
		id = int(input('Informe o ID do contrato a ser deletado: '))
		i = id - 1
		print("ID = ",id ,"\n", list_contrato[i],"\n")
		list_contrato.pop(i)
		print("contrato deletado!")

# Delete Imóvel by ID
def delete_byid_imovel():
	if len(list_imovel) == 0:
		is_empty()
	else:
		listar_all_imovel()
		id = int(input('Informe o ID do imovel a ser deletado: '))
		i = id - 1
		print("ID = ",id ,"\n", list_imovel[i],"\n")
		list_imovel.pop(i)
		print("imovel deletado!")

# Delete all clientes
def delete_all_cliente():
	if len(list_cliente) == 0:
		is_empty()
	else:
		list_cliente.clear()
		print('Todos os Clientes foram deletados com Sucesso.')

# Delete all Contratos
def delete_all_contrato():
	if len(list_contrato) == 0:
		is_empty()
	else:
		list_contrato.clear()
		print('Todos os Contratos foram deletados com Sucesso.')

# Delete all Imóveis
def delete_all_imovel():
	if len(list_imovel) == 0:
		is_empty()
	else:
		list_imovel.clear()
		print('Todos os Imóveis foram deletados com Sucesso.')

#-------------GERAR CONTRATO MODULE

# One alternative to generate Contratos by getting the position of below specified keys to generate and add it to the list_contrato list,
# using a variable "catch_" to transform ID in position. More fields and parameters can be added as necessary.
def gerar_contrato():
	# Aqui poderemos incluir uma validação/verificação de dados
	catch_locador = (int(input('Informe o ID do Cliente Locador: '))) - 1
	catch_locatario = (int(input('Informe o ID do Cliente Locatário: '))) - 1
	catch_imovel_objeto = (int(input('Informe o ID do Imóvel: '))) - 1
	termos = (input('Informe os termos do Contrato: '))
	pos_locador = list_cliente[catch_locador]["Documento"]
	pos_locatario = list_cliente[catch_locatario]["Documento"]
	pos_imovel = list_imovel[catch_imovel_objeto]["Matrícula"]
	registro_contrato = {"Locador":pos_locador, "Locatário":pos_locatario, "Imóvel Objeto":pos_imovel, "Termos":termos}
	list_contrato.append(registro_contrato)
	print(pos_locador)
	print("Sucesso! Cadastrado!")
	catch_locador = 0
	catch_locatario = 0
	catch_imovel_objeto = 0

#-------------MISCELLANEOUS FUNCTIONS

# Starting CRUD application and printing welcome user message:
def welcome():
	#Add login here, if necessary
	usuario = input("Entre com o seu nome: ")
	if usuario == "":
		print("Seja Bem-vindo(a), pessoa!\n")
	else:
		print(f"Seja Bem-vindo(a), {usuario}!\n")
	main_menu()

# This is for exiting the program:			
def exit_program():
	print("Saindo do sistema...")
	exit()

# This is for invalid option:
def try_again():
	print("Opção Inválida! Tente novamente.")

# For when a list is empty:
def is_empty():
	print("Não há nada aqui...")

# When a confirmation is needed:
def areyousure():
	opcao = int(input("Tem certeza que deseja continuar?\n1 - Sim\n2 - Não\n"))
	if not opcao in [1,2]:
		try_again()
	if opcao == 1:
		print('Confirmação recebida.')
	elif opcao == 2:
		print("Retorando ao menu principal...")
		main_menu()

#-------------ACTUAL PROGRAM START
# Speak, friend, and enter:
# Mellon
# Notice: This is a reference to a very good collection of books and movies.
welcome()