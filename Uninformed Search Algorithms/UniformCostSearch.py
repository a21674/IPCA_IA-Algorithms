# Uniform-cost search is an uninformed search algorithm that uses the lowest cumulative cost 
# to find a path from the source to the destination. Nodes are expanded, starting from the root, 
# according to the minimum cumulative cost. The uniform-cost search is then implemented using a Priority Queue.

# The Algorithm 
# 1: Insert the root node into the priority queue
# 2: Repeat while the queue is not empty:
#   - Remove the element with the highest priority
#   - If the removed node is the destination, print total cost and stop the algorithm
#   - Else, enqueue all the children of the current node to the priority queue, with their cumulative cost from the root as priority
# https://www.educative.io/answers/what-is-uniform-cost-search


graph = {
    'A': [('B', 5), ('C', 7)],
    'B': [('D', 8), ('E', 1)],
    'C': [('D', 9), ('G', 13)],
    'D': [('G', 4), ('F', 7), ('I', 5)],
    'E': [],    
    'F': [],
    'I': [('G', 14)],
    'G': [],
}


def path_cost(path):
    total_cost = 0
    for (node, cost) in path:
        total_cost += cost
    return total_cost, path[-1][0] # retorna 2 possibilidades de ordenação, primeiro o custo total, caso seja igual a outro caminho, será ordenado por ordem alfabética


def ucs(graph, start, goal):
    queue = [[(start, 0)]]
    visited = []

    while queue:
        queue.sort(key = path_cost()) # Orderna a fila pelo caminho mais curto até ao momento
        path = queue.pop(0) # atribui o primeiro node (menor custo) e remove-o da fila para ser avaliado novamente pelo ultimo node
        node = path[-1][0] # devolve o nome do node

        if node in visited:
            continue # não avança volta á itereção com o while

        visited.append(node)

        if node == goal:
            print(path)
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for (node2, cost) in adjacent_nodes:
                new_path = path.copy() # clona o caminho original
                new_path.append([node2, cost]) # adiciona o adjacente e o seu custo ao novo caminho
                queue.append(new_path)


ucs(graph, 'A', 'G')