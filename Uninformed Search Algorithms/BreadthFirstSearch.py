# Breadth-first search (BFS) is an algorithm used for tree traversal on graphs or tree data structures. 
# BFS can be easily implemented using recursion and data structures like dictionaries and lists.
# The Algorithm
# 1 - Pick any node, visit the adjacent unvisited vertex, mark it as visited, display it, and insert it in a queue.
# 2 - If there are no remaining adjacent vertices left, remove the first vertex from the queue.
# 3 - Repeat step 1 and step 2 until the queue is empty or the desired node is found.

#       A
#      / \
#     B   C
#    / \   \
#   D   E-> F


# Versão sem estado objectivo que visita todos os nós em pronfudidade
def bfs(visited, graph, start_node):
    visited.append(start_node)
    queue.append(start_node)
    
    print('Nó visitado:')
    while queue:
        atual = queue.pop(0) # guarda o nó atual e remove-o o da fila de nós a visitar
        print(atual, end = ' ') #colocar tudo na mesma linha
        for neighbour in graph[atual]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour) # guarda na fila de nós a explorar os seus vizinhos

     
     
                  
visited = [] # List to keep track of visited nodes.
queue = [] #list that is used to keep track of nodes currently in the queue

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

bfs(visited, graph, 'A')