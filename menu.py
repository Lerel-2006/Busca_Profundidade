
# Busca em Profundidade (DFS)

import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def criarGrafo():
    return {}


def imprimirGrafo(grafo):
    print("-" * 40)

    for vertice in grafo:
        print(vertice, ": ", grafo[vertice])

    print("-" * 40)


def inserirVertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []
    else:
        print("Esse vértice já existe")


def inserirArestaDirecionada(grafo, origem, destino):
    if origem in grafo and destino in grafo:
        grafo[origem].append(destino)
    else:
        print("Um ou ambos os vértices não existem")


def inserirArestaNaoDirecionada(grafo, origem, destino):
    if origem in grafo and destino in grafo:
        grafo[origem].append(destino)
        grafo[destino].append(origem)
    else:
        print("Um ou ambos os vértices não existem")


def listarVizinhosVertice(grafo, vertice):
    lista = []

    if vertice in grafo:
        for v in grafo[vertice]:
            lista.append(v)

    return lista



def buscaEmProfundidade(grafo, inicio):
    visitados = []
    pilha = []

    if inicio not in grafo:
        print("O vértice inicial não existe nesse grafo")
        return None

    pilha = [inicio]

    while pilha:
        atual = pilha.pop()

        if atual not in visitados:
            visitados.append(atual)

            vizinhos = listarVizinhosVertice(grafo, atual)

            for vizinho in vizinhos:
                if vizinho not in visitados and vizinho not in pilha:
                    pilha.append(vizinho)

    return visitados



def detectarCiclo(grafo):
    visitados = []
    pilha = []

    for inicio in grafo:

        if inicio not in visitados:
            pilha.append({
                'vertice': inicio,
                'pai': None
            })

            while pilha:
                atual = pilha.pop()

                vertice = atual['vertice']
                pai = atual['pai']

                if vertice not in visitados:
                    visitados.append(vertice)

                    vizinhos = listarVizinhosVertice(grafo, vertice)

                    for vizinho in vizinhos:

                        na_pilha = any(
                            item['vertice'] == vizinho
                            for item in pilha
                        )

                        if vizinho not in visitados and not na_pilha:
                            pilha.append({
                                'vertice': vizinho,
                                'pai': vertice
                            })

                        elif vizinho != pai:
                            print("O grafo possui ciclo!")
                            return True

    print("O grafo não possui ciclo!")
    return False



def menu():
    grafo = {}

    while True:
        print("=" * 40)
        print("Qual o tipo de Grafo que você deseja?")
        print("0 - Sair")
        print("1 - Direcionado")
        print("2 - Não Direcionado")
        print("=" * 40)

        op = input("Digite uma opção: ")

        if op == "0":
            print("Sistema finalizado")
            return

        elif op == "1":
            direcionado = True
            break

        elif op == "2":
            direcionado = False
            break

        else:
            limpar_tela()
            print("Opção inválida, tente novamente")

    while True:
        print("=" * 40)
        print(" " * 12, "MENU DFS")
        print("=" * 40)
        print("0 - Sair")
        print("1 - Mostrar o Grafo")
        print("2 - Inserir Vértice")
        print("3 - Inserir Aresta")
        print("4 - Busca em Profundidade (DFS)")
        print("5 - Detectar Ciclos (DFS)")
        print("=" * 40)

        opcao = input("Digite uma opção: ")

        if opcao == "0":
            print("Sistema de grafos finalizado...")
            break

        elif opcao == "1":
            imprimirGrafo(grafo)

        elif opcao == "2":
            vertice = input("Vértice a ser inserido: ").upper()

            inserirVertice(grafo, vertice)
            imprimirGrafo(grafo)

        elif opcao == "3":
            origem = input("Vértice Origem da aresta: ").upper()
            destino = input("Vértice Destino da aresta: ").upper()

            if direcionado:
                inserirArestaDirecionada(grafo, origem, destino)
            else:
                inserirArestaNaoDirecionada(grafo, origem, destino)

            imprimirGrafo(grafo)

        elif opcao == "4":
            inicio = input("Digite o vértice inicial: ").upper()

            resultado = buscaEmProfundidade(grafo, inicio)

            if resultado != None:
                print("Ordem dos vértices visitados:", resultado)

        elif opcao == "5":

            if direcionado:
                print("A detecção de ciclos desta atividade")
                print("é destinada a grafos não direcionados.")

            else:
                if not grafo:
                    print("O grafo está vazio")
                else:
                    detectarCiclo(grafo)

        else:
            print("Opção inválida, tente novamente")


menu()
