# Problema: Maximizar o lucro de um transporte de produtos
# Restrição: - Capacidade máxima do camião 3m^3
#            - Total de espaço dos produtos todos = 4.79m^3

from math import prod
import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose


produtos = [('Refrigerador A', 0.751, 999.90),
            ('Celular', 0.0000899, 2911.12),
            ('TV 55', 0.400, 4346.99),
            ('TV 50', 0.290, 3999.90),
            ('TV 42', 0.200, 2999.00),
            ('Notebook A', 0.00350, 2499.90),
            ('Ventilador', 0.496, 199.90),
            ('Microondas A', 0.0424, 308.66),
            ('Microondas B', 0.0544, 429.90),
            ('Microondas C', 0.0319, 299.29),
            ('Refrigerador B', 0.635, 849.00),
            ('Refrigerador C', 0.870, 1199.89),
            ('Notebook B', 0.498, 1999.90),
            ('Notebook C', 0.527, 3999.00)]

capacidade_camiao = 3 # 3m^3



def imprimir_solucao(solucao):
    custo_total = 0
    espaco_ocupado = 0
    for i in range(len(solucao)):
        if solucao[i] == 1: # 1 = produto transportado, 0 = produto não transportado
            custo_total += produtos[i][2]
            espaco_ocupado += produtos[i][1]
            print('%s - %s' % (produtos[i][0], produtos[i][2])) # nome e preço
    print('\nCusto Total: ', custo_total)
    print('Total Espaço Ocupado: ', espaco_ocupado)        
    
            
################ Fitness Function #################
# função responsavel por calcular o custo de uma solução
def fitness_function(solucao):
    custo_total = 0
    espaco_ocupado = 0
    for i in range(len(solucao)):
        if solucao[i] == 1: #produto transportado
            custo_total += produtos[i][2]
            espaco_ocupado += produtos[i][1]
    
    if espaco_ocupado > capacidade_camiao:
        custo_total = 1 #Penalização por ultrapassar o espaço excedido
    
    return custo_total


#solucao1 = [0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0 , 1]
#imprimir_solucao(solucao1)
#print(fitness_function(solucao1))




###### Uso da Biblioteca Mlrose que já contém algoritmos de otimização prontos a usar #######
# (https://mlrose.readthedocs.io/en/stable/source/intro.html)

fitness_func = mlrose.CustomFitness(fitness_function)
problem = mlrose.DiscreteOpt(length=14, # qtd de produtos
                             fitness_fn=fitness_func, # função fitness personalizada
                             maximize=True, # é pretendido maximizar lucro
                             max_val=2) # 0 = não é transportado; 1 = é transportado



########################### Algoritmo Hill Climb ###########################

melhor_solucao, melhor_custo = mlrose.hill_climb(problem)
#imprimir_solucao(melhor_solucao)



########################### Simulated Annealing ###########################

melhor_solucao, melhor_custo = mlrose.simulated_annealing(problem, 
                                                          #schedule=mlrose.ArithDecay(), #metodos de otimização e parametros que permitem afinar o algoritmo
                                                          schedule=mlrose.GeomDecay(init_temp=10000),
                                                          #schedule=mlrose.ExpDecay()
                                                          random_state=1 #irá sempre apresentar o mesmo valor para todas as execuções, caso contrario ele irá proceder a um novo processo random
                                                          )
#imprimir_solucao(melhor_solucao)



########################### Algoritmo Genético ###########################

melhor_solucao, melhor_custo = mlrose.genetic_alg(problem, 
                                                  pop_size=500, 
                                                  mutation_prob=0.2 #20% probabilidade de acontecer mutação
                                                  )
imprimir_solucao(melhor_solucao)