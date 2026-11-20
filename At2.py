#Detectar ciclos
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B', 'D'],
    'D': ['C']
}


def listarVizinhosVertice(grafo, vertice):
    lista = []

    if vertice in grafo:
        for v in grafo[vertice]:
            lista.append(v)

    return lista


def detectarCiclo(grafo):
    visitados = []
    pilha = []
    possuiCiclo = False

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
                            possuiCiclo = True

    print("Vértices visitados:", visitados)

    if possuiCiclo:
        print("O grafo possui ciclo!")
    else:
        print("O grafo não possui ciclo!")

    return possuiCiclo


detectarCiclo(grafo)
