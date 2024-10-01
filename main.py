from time import sleep

listaEstoque = ['Lápis', 'Caneta']

#menu principal
print('Bem vindo ao controlador do estoque!')
opc = 0
while opc != 6:
    try:
        opc = int(input('Digite a função desejada: \n [1] Consultar estoque \n [2] Consultar código de item \n [3] Cadastrar item \n [4] Editar item \n [5] Excluir item\n [6] Sair do aplicativo\n'))
            #consultar estoque
        while True:
            if opc == 1:
                print('Seu estoque atual contém os itens:')
                print('Código | Descrição')
                for k, v in enumerate(listaEstoque):
                    print(f'{k} | {v}.')
                cont = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
                if cont == 'N':
                    print("Voltando ao menu principal...")
                    break
            #procurar item       
            elif opc == 2:
                proc = input('Digite o nome do item: ')
                indiceProc = listaEstoque.index(proc)
                if proc in listaEstoque:
                    print(f'O código do item {proc} é {indiceProc}')
                cont = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
                if cont == 'N':
                    print("Voltando ao menu principal...")
                    break
            #cadastrar item
            elif opc == 3:
                add = input("Digite o nome do item que quer cadastrar: ")
                listaEstoque.append(add)
                indiceAdd = listaEstoque.index(add)
                print(f'O item {add} foi cadastrado com o código {indiceAdd}')
                cont = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
                if cont == 'N':
                    print("Voltando ao menu principal...")
                    break
            #editar item
            elif opc == 4:
                edit = int(input('Digite o código do produto que será editado: '))
                procEstoq = listaEstoque[edit]
                novoNome = input(f'Digite a nova descrição para o item {procEstoq}: ')
                listaEstoque.insert(edit, novoNome)
                listaEstoque.remove(procEstoq)
                cont = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
                if cont == 'N':
                    print("Voltando ao menu principal...")
                    break
            #excluir item
            elif opc == 5:
                excluir = int(input('Digite o código do produto que será removido: '))
                procEstoq = listaEstoque[excluir]
                listaEstoque.remove(procEstoq)
                print(listaEstoque)
                cont = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
                if cont == 'N':
                    print("Voltando ao menu principal...")
                    break
            elif opc == 6:
                print('Saindo do programa...')
                sleep(1)
                print('Adeus!')
                break
            else:
                print("Digite um valor entre 1 e 6.")
                break
    except ValueError:
        print('Favor, digitar um valor em número!')