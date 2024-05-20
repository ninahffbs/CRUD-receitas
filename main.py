from classes import Receita

while True:
    opcao = int(input(f"""\nDigite a opção desejada:
[1] Adicionar
[2] Visualizar
[3] Atualizar
[4] Excluir
[5] Filtrar por país
[6] Lista de favoritos
[7] Sair 
"""))

    if opcao == 7:
        break

    if opcao == 1:

        nomeInput = input("Digite o nome: ").capitalize()

        origemInput = input("Digite a origem: ").capitalize()
        
        ingredientesLista = input("Digite os ingredientes(separados por ; ): ").split(";")
        
        modo_de_preparoInput = input("Digite o modo de preparo: ")

        receita = Receita(nomeInput, origemInput, ingredientesLista, modo_de_preparoInput)

        # print(f"""Nome: {receita.nome}
        # Origem: {receita.origem}
        # Ingredientes: {receita.ingredientes}
        # Modo de preparo: {receita.modo_de_preparo}""")
        
        receita.adicionar(receita)

    elif opcao == 2:
        Receita.visualizarTodas()
        receita = input("\nDigite o nome da receita desejada: ").capitalize()
        Receita.buscarReceita(receita)

    elif opcao == 3:
        pass
    
    elif opcao == 4:
        Receita.visualizarTodas()
        excluir = input("\nDigite o nome da receita que deseja excluir: ").capitalize()
        Receita.exclusao(excluir)
        print("Receita excluída com sucesso!")

    elif opcao == 5:
        nacionalidade = input("Insira de qual país você deseja visualizar as receitas: ").capitalize()
        Receita.filtrarPais(nacionalidade)
    