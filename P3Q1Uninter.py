
# Representa cada paciente da fila
class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None


# Controla a fila de atendimento
class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.contador_verde = 1
        self.contador_amarelo = 201

    # Adiciona o paciente verde no final da fila
    def inserirSemPrioridade(self, nodo):
        atual = self.head

        while atual.proximo != None:
            atual = atual.proximo

        atual.proximo = nodo

    # Adiciona o paciente amarelo antes dos verdes
    def inserirComPrioridade(self, nodo):
        if self.head.cor == "V":
            nodo.proximo = self.head
            self.head = nodo
            return

        atual = self.head

        # Procura o último paciente amarelo
        while atual.proximo != None and atual.proximo.cor == "A":
            atual = atual.proximo

        nodo.proximo = atual.proximo
        atual.proximo = nodo

    # Cadastra um paciente na fila
    def inserir(self):
        cor = input("Informe a cor do cartão (A/V): ").upper()

        if cor != "A" and cor != "V":
            print("Cor inválida! Digite A ou V.")
            return

        # Define o número do cartão automaticamente
        if cor == "V":
            numero = self.contador_verde
            self.contador_verde += 1
        else:
            numero = self.contador_amarelo
            self.contador_amarelo += 1

        novo = Nodo(numero, cor)

        if self.head == None:
            self.head = novo
        elif cor == "V":
            self.inserirSemPrioridade(novo)
        else:
            self.inserirComPrioridade(novo)

        print(f"Paciente adicionado: Cartão {cor}, número {numero}")

    # Mostra todos os pacientes na ordem de atendimento
    def imprimirListaEspera(self):
        if self.head == None:
            print("A fila de espera está vazia.")
            return

        print("Lista de espera:")
        atual = self.head

        while atual != None:
            print(f"[{atual.cor}, {atual.numero}]", end=" -> ")
            atual = atual.proximo

        print("None")

    # Chama e remove o primeiro paciente da fila
    def atenderPaciente(self):
        if self.head == None:
            print("Não existem pacientes na fila.")
            return

        paciente = self.head
        print(f"Atendendo o paciente cartão cor {paciente.cor} e número {paciente.numero}")

        self.head = self.head.proximo


# Menu principal
fila = ListaEncadeada()

while True:
    print("\n===== SISTEMA DE TRIAGEM HOSPITALAR =====")
    print("1 - Adicionar paciente à fila")
    print("2 - Mostrar pacientes na fila")
    print("3 - Chamar paciente")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        fila.inserir()
    elif opcao == "2":
        fila.imprimirListaEspera()
    elif opcao == "3":
        fila.atenderPaciente()
    elif opcao == "4":
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")
