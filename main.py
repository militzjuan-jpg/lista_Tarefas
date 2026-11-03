import emoji

def menu_main():
    print("Gerenciador de tarefas \n")
    print("""
          --------------------------------------- MENU -----------------------------------------


          1. Adicionar tarefa
          2. Marcar tarefa como concluída
          3. Listar tarefas
          4. Deletar items
          5. Sair

    """)
    op = int(input("Digite a opção na qual deseja prosseguir: "))
    return op

opcao = menu_main()

lista_De_Tarefas = []

while True:
    if opcao == 1:
        
        while True:
            tarefa = input("Digite as tarefa e pressione enter entre cada uma(caso deseje finalizar digite 'ok'): ")
            if tarefa == 'ok' or tarefa == "'ok'":
                break
            lista_De_Tarefas.append(tarefa)

        lista_Enumerada = dict(enumerate(lista_De_Tarefas, start=1))
        opcao = menu_main()
    elif opcao== 2:
        
        for chave, valor in lista_Enumerada.items():
            print(f"{chave}: {valor}")

        while True:
            item =input("Digite o numero da tarefa que deseja marcar como concluída(para finalizar digite 'ok'): ")
            if item == "ok" or item=="'ok'":
                break
            else:
                item = int(item)
                lista_Enumerada[item] =lista_Enumerada[item] + " ✅"
            
               
            

        opcao = menu_main()
    elif opcao== 3:
        for chave, valor in lista_Enumerada.items():
            print(f"{chave}: {valor}")

        input("Para continuar aperte enter: ")
        opcao = menu_main()
    elif opcao ==4:
    
        for chave, valor in lista_Enumerada.items():
            print(f"{chave}: {valor}")

        while True:
            try:
                item = int(input("digite o numero do item a ser deletado: "))
                
                if item not in lista_Enumerada.keys():
                    print("Número digitado não consta na lista! tente novamente.")
                    break
                else:
                    lista_Enumerada.pop(item)
                
                for chave, valor in lista_Enumerada.items():
                    print(f"{chave}: {valor}")
                
                input("Pressione enter para continuar: ")
                break
                
            except ValueError:
                print("caracter incorreto! digite um numero válido: ")

       

        opcao = menu_main()
        
    elif opcao== 5:
        break
    else:
        print("Número digitado está incorreto! Por favor tente novamente.")
        opcao = menu_main()