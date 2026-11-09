import emoji
def criar_lista():
    print("""
        1.Criar nova lista de tarefas.
        2.Abrir lista já existente.   
    """)
    try:
        opcao_escolhida = int(input("digite a opção na qual deseja prosseguir: "))
        if opcao_escolhida !=1 and opcao_escolhida !=2:
            print("número incorreto! tente novamente.")
            criar_lista()
        elif opcao_escolhida ==2:
            try:
                lista = input("Digite o nome do arquivo (sem extensão): ")
                nome_lista = f"{lista}.txt"
                with open(nome_lista, "r", encoding="utf-8") as arquivo:
                    conteudo = arquivo.read()
                    print(conteudo)
                    input("Pressione a tecla 'Enter' para continuar: ")
                    return nome_lista
            except FileNotFoundError:
                print("Erro: O arquivo especificado não foi encontrado.")
        else:
            try:
                titulo_lista = input("Digite o nome da sua lista (sem a extensão): ")
                titulo_final = f"{titulo_lista}.txt"
                with open(titulo_final, "x", encoding="utf-8") as arquivo:
                    arquivo.write("")
                    return titulo_final
            except FileExistsError:
                print("Erro! Este arquivo já existe.")
                criar_lista()
    except ValueError:
        print("Valor incorreto! Digite um número.")
        criar_lista()

def menu_main():         #menu principal
    print("Gerenciador de tarefas \n")
    print("""
          --------------------------------------- MENU -----------------------------------------


          1. Adicionar tarefa
          2. Modificar tarefa
          3. Marcar tarefa como concluída
          4. Listar tarefas
          5. Deletar items
          6. Sair

    """)
    op = int(input("Digite a opção na qual deseja prosseguir: "))
    return op

lista = criar_lista()

opcao = menu_main() #primeira operação do programa, chamar o menu.

lista_De_Tarefas = [] 

while True:
    if opcao == 1: #adicionar tarefas
        
        while True:
            tarefa = input("Digite as tarefa e pressione enter entre cada uma(caso deseje finalizar digite 'ok'): ") #se mantém no loop até o usário digitar 'ok', podendo colocar variás tarefas de uma vez sem voltar ao menu
            if tarefa == 'ok' or tarefa == "'ok'":
                break
            lista_De_Tarefas.append(tarefa)

        lista_Enumerada = dict(enumerate(lista_De_Tarefas, start=1)) #transforma a lista, com as tarefas colocadas pelo usuário, em um dicionário enumerado
        opcao = menu_main()
    elif opcao == 2: #modificar tarefas
        for chave, valor in lista_Enumerada.items():
            print(f"{chave}: {valor}")

        try:
            item = int(input("Digite o número do item que deseja modificar: "))
            for chave in lista_Enumerada.keys():
                if chave == item:
                    item_modificado = input("digite a nova tarefa neste item: ")
                    lista_Enumerada[chave]=item_modificado

            for chave in lista_Enumerada.keys():
                if chave != item:
                    print("Valor não existe na lista! Você irá ser redirecionado ao menu.")
                    opcao = menu_main()
                      
        except ValueError:
            print("valor incorreto! Digite um número. Você ira ser redirecionado ao menu noavamente.")
            opcao = menu_main()
    elif opcao== 3: #marcar tarefas concluídas
        
        for chave, valor in lista_Enumerada.items():
            print(f"{chave}: {valor}")

        while True:
            item =input("Digite o numero da tarefa que deseja marcar como concluída(para finalizar digite 'ok'): ") #usuário pode ir colocando os items qu estão concluídos de uma vez só, depois pressiona 'ok' para finalizar
            if item == "ok" or item=="'ok'":
                break
            else:
                item = int(item)
                lista_Enumerada[item] =lista_Enumerada[item] + " ✅"

        for chave, valor in lista_Enumerada.items():
                    print(f"{chave}: {valor}")
            
        opcao = menu_main()
    elif opcao== 4: #listar tarefas
        for chave, valor in lista_Enumerada.items(): #lista os items do dicionário
            print(f"{chave}: {valor}")

        input("Para continuar aperte enter: ")
        opcao = menu_main()
    elif opcao ==5: #deletar tarefas
    
        for chave, valor in lista_Enumerada.items():
            print(f"{chave}: {valor}")

        while True:
            try:
                item = int(input("digite o numero do item a ser deletado: "))
                
                if item not in lista_Enumerada.keys():
                    print("Número digitado não consta na lista! tente novamente.") #verifica se o número digitado está nas chaves do dicionário
                    break
                else:
                    lista_Enumerada.pop(item) # se está, o item(chave e valor) é deletado
                
                lista_Enumerada = {novo_index: valor for novo_index, valor in enumerate(lista_Enumerada.values(), start=1)} #reorganiza as chaves dos itens da lista

                for chave, valor in lista_Enumerada.items():
                    print(f"{chave}: {valor}")
                
                input("Pressione enter para continuar: ")
                break
                
            except ValueError:
                print("caracter incorreto! digite um numero válido: ")

       

        opcao = menu_main()
        
    elif opcao== 6: #encerra o loop e o programa
        break
    else: #se o numero foi digitado incorretamente, chama o menu novamente para corrigir o erro.
        print("Número digitado está incorreto! Por favor tente novamente.")
        opcao = menu_main()