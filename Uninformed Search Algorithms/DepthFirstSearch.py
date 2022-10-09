# Depth-first search (DFS), is an algorithm for tree traversal on graph or tree data structures. 
# It can be implemented easily using recursion and data structures like dictionaries and sets.
# The Algorithm
# 1 - Pick any node. If it is unvisited, mark it as visited and recur on all its adjacent nodes.
# 2 - Repeat until all the nodes are visited, or the node to be searched is found


# Versão sem estado objectivo que visita todos os nós em pronfudidade
def dfs(visited, graph, start_node):
    if start_node not in visited:
        print ("Atual node: ", start_node)
        visited.append(start_node)
        for neighbour in graph[start_node]:
            dfs(visited, graph, neighbour)


# Versão que recebe um nó como estado objectivo dando o custo para as várias possibilidades
def dfs_wiht_target(graph, start_node, target_node, count = 0):
    if start_node == target_node:
        print("Chegou ao objectivo com um custo de:", count)
        return
    print ("Atual node: ", start_node)
    print('Adjacentes de', start_node)
    for i in graph[start_node]:
        print('-', i)
    count += 1
    for neighbour in graph[start_node]:
        dfs_wiht_target(graph, neighbour, target_node, count)


if __name__ == "__main__":
    # Using a Python dictionary to act as an adjacency list
    graph = {
        'A' : ['B','C'],
        'B' : ['D', 'E'],
        'C' : ['F', 'G'],
        'D' : ['H', 'I'],
        'E' : ['J', 'K'],
        'F' : ['E', 'L', 'M'],
        'G' : [],
        'H' : [],
        'I' : [],
        'J' : [],
        'K' : [],
        'L' : [],
        'M' : [],
    }

    visited = [] # Array to keep track of visited nodes.
    #dfs(visited, graph, 'A')
    dfs_wiht_target(graph, 'A', 'K')