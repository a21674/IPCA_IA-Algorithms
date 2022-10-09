# Same as Breadth Search but now the path has costs 
# The Algorithm
# 1.  A graph search algorithm tries to find an optimal solution using cost.
# 2.  Expands nodes with the lowest path cost.
# 3.  Uses a priority queue for the frontier, sorted by path cost.
# 4.  Problem definition:
# Example:
#       A
#      / \
#     B   C
#    / \   \
#   D   E-> F

class Vertice:
    def __init__(self, nome) -> None:
        self.nome = nome        
        self.adjacentes = []

    def add_adjacentes(self, adjacente):
        self.adjacentes.append(adjacente)

    def show_adjacentes(self):
        for i in self.adjacentes: # i tem a estrutura do Adjacente
            print('Vertice: {} - Custo: {}'.format(i.vertice.nome, i.custo))

class Adjacente:
    def __init__(self, vertice, custo) -> None:
        self.vertice = vertice #será to tipo Vertice
        self.custo = custo
         
class Grafo:
    A = Vertice('A')
    B = Vertice('B')
    C = Vertice('C')
    D = Vertice('D')
    E = Vertice('E')
    F = Vertice('F')
    
    A.add_adjacentes(Adjacente(B, 5))
    A.add_adjacentes(Adjacente(C, 7))
    B.add_adjacentes(Adjacente(D, 2))
    B.add_adjacentes(Adjacente(F, 6))
    C.add_adjacentes(Adjacente(F, 10))
    E.add_adjacentes(Adjacente(F, 3))
    

# Versão sem estado objectivo que visita todos os nós em pronfudidade
def ucs(visited, start_node, target_node):
    
    visited.append(start_node)
    queue.append(start_node)
    path = []
    count = 0
    print('Nó visitado:')
    while queue: # while the queue is not empty
        
        atual = queue.pop(0) # guarda o nó atual e remove-o o da fila de nós a visitar
        
        print(atual.nome, end = ' ') # end = ' ' coloca tudo na mesma linha
        for neighbour in atual.adjacentes:
            if neighbour not in visited:
                path.append({atual, neighbour.vertice})
                if neighbour.vertice == target_node:
                    print ('Caminho encontrado. O custo foi de:', count)
                    return
                count += neighbour.custo
                visited.append(neighbour.vertice)
                queue.append(neighbour.vertice) # guarda na fila de nós a explorar os seus vizinhos

     

if __name__ == "__main__":                  
    visited = [] # List to keep track of visited nodes.
    queue = [] #list that is used to keep track of nodes currently in the queue
    grafo = Grafo()
    grafo.A.show_adjacentes()
    
    ucs(visited, grafo.A, grafo.F)