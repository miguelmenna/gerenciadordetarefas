tarefas = []

def mostrar_menu():
    print("** Menu **")
    print("1. Adicionar nova tarefa")
    print("2. Listar todas as tarefas")
    print("3. Remover tarefa")
    print("4. Sair")

def adicionar_tarefa():
    nome_tarefa = input("Digite o nome da tarefa: ")
    tarefas.append(nome_tarefa)

def listar_tarefas():
    if len(tarefas) == 0:
        print("Não há tarefas cadastradas.")
        return
    for i, tarefa in enumerate(tarefas):
        print(f"{i}. {tarefa}")

def remover_tarefa():
    if len(tarefas) == 0:
        print("Não há tarefas cadastradas.")
        return
    try:
        indice = int(input("Digite o índice da tarefa a ser removida: "))
        if indice < 0 or indice >= len(tarefas):
            print("Índice inválido.")
            return
        tarefas.pop(indice)
        print("Tarefa removida com sucesso.")
    except ValueError:
        print("Por favor, digite um número inteiro para o índice.")

def main():
    mostrar_menu()
    while True:
        try:
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                adicionar_tarefa()
            elif opcao == 2:
                listar_tarefas()
            elif opcao == 3:
                remover_tarefa()
            elif opcao == 4:
                print("Saindo do programa. Até mais!")
                break
            else:
                print("Opção inválida.")
        except ValueError:
            print("Por favor, digite um número inteiro para a opção.")

if __name__ == "__main__":
    main()