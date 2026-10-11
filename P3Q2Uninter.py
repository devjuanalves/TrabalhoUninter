
# Representa um estado na lista encadeada
class Nodo:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None


# Gerencia a tabela hash
class TabelaHash:
    def __init__(self):
        self.tabela = [None] * 10

    # Calcula a posição usando os valores ASCII
    def hash(self, sigla):
        if sigla == "DF":
            return 7

        letra1 = ord(sigla[0])
        letra2 = ord(sigla[1])

        return (letra1 + letra2) % 10

    # Adiciona um estado no início da lista
    def inserir(self, sigla, nomeEstado):
        posicao = self.hash(sigla)
        novo = Nodo(sigla, nomeEstado)

        novo.proximo = self.tabela[posicao]
        self.tabela[posicao] = novo

    # Percorre e imprime as posições da tabela
    def imprimirTabela(self):
        for posicao in range(10):
            print(f"{posicao}: ", end="")

            atual = self.tabela[posicao]

            while atual is not None:
                print(f"{atual.sigla} -> ", end="")
                atual = atual.proximo

            print("None")


# Cria a tabela hash
tabela = TabelaHash()

# Teste 1: mostra a tabela vazia
print("===== TABELA HASH VAZIA =====")
tabela.imprimirTabela()


# Estados brasileiros e Distrito Federal
estados = [
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AP", "Amapá"),
    ("AM", "Amazonas"),
    ("BA", "Bahia"),
    ("CE", "Ceará"),
    ("DF", "Distrito Federal"),
    ("ES", "Espírito Santo"),
    ("GO", "Goiás"),
    ("MA", "Maranhão"),
    ("MT", "Mato Grosso"),
    ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"),
    ("PA", "Pará"),
    ("PB", "Paraíba"),
    ("PR", "Paraná"),
    ("PE", "Pernambuco"),
    ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"),
    ("RR", "Roraima"),
    ("SC", "Santa Catarina"),
    ("SP", "São Paulo"),
    ("SE", "Sergipe"),
    ("TO", "Tocantins")
]

# Insere os 27 registros na tabela
for sigla, nome in estados:
    tabela.inserir(sigla, nome)


# Teste 2: mostra a tabela com os estados
print("\n===== TABELA HASH COM 27 ESTADOS =====")
tabela.imprimirTabela()


# Solicita o nome para criar o estado fictício
nome_ficticio = input("\nDigite seu nome completo: ")

partes_nome = nome_ficticio.strip().split()

if len(partes_nome) >= 2:
    # Usa a primeira letra do nome e do último sobrenome
    sigla_ficticia = (partes_nome[0][0] + partes_nome[-1][0]).upper()

    tabela.inserir(sigla_ficticia, nome_ficticio)

    # Teste 3: mostra a tabela completa
    print("\n===== TABELA HASH COMPLETA =====")
    tabela.imprimirTabela()
else:
    print("Informe o nome e o sobrenome.")
