#Busca em Profundidade
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

def buscaEmProfundidade(grafo, inicio):
  visitados = []
  pilha = []

  if inicio not in grafo:
    print("O vértice inicial NÂO existe nesse grafo, tente outro")
  else:
    pilha = [inicio]

    while pilha:
      atual = pilha.pop()
      if atual not in visitados:
        visitados.append(atual)
        vizinhos = listarVizinhosVertice(grafo, atual)
        #print(pilha)

        for vizinho in vizinhos:
          if vizinho not in visitados and vizinho not in pilha:
            pilha.append(vizinho)

    return visitados

res = buscaEmProfundidade(grafo, "A")
print(res)