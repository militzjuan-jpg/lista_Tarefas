def menu_main():
    print("Gerenciador de tarefas \n")
    print("""
          --------------------------------------- MENU -----------------------------------------


          1. Adicionar tarefa
          2. Marcar tarefa como concluída
          3. Listar tarefas
          4. Sair

    """)
    op = int(input("Digite a opção na qual deseja prosseguir: "))
    return op

opcao = menu_main()

lista_De_Tarefas = []

while True:
    if opcao ==1:
        tarefa = input("Digite a tarefa: ")
        lista_De_Tarefas.append(tarefa)
        menu_main()
    elif opcao==2:
        pass
    elif opcao==3:
        pass
    elif opcao==4:
        break
    else:
        print("Número digitado está incorreto! Por favor tente novamente.")
        opcao = menu_main()