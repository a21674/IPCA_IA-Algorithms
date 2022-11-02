# Desafio, 6 pessoas de diferentes países pretendem encontrar-se para uma reunião
# num outro ponto do mapa (no caso Roma). No fim da reunião devem regressar aos seus países de origem
# Objectivo: Minimizar os custos dos bilhetes de Ida e Volta
# Restrição: Todas as pessoas devem chegar num horário identico e partir tb num horário identico


import os
import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose

## Estrutura do Problema
local_pessoas = [('Lisboa', 'LIS'),
                ('Madrid', 'MAD'),
                ('Paris', 'CDG'),
                ('Dublin', 'DUB'),
                ('Bruxelas', 'BRU'),
                ('Londres', 'LHR')]

local_destino = 'FCO'

# Carregar BD com voos num dicionario
voos = {}
for linha in open(os.path.join(sys.path[0], 'flights.txt'), 'r'):
  #print(linha.split(','))
  origem, destino, saida, chegada, preco = linha.split(',') #ira armazenar cada valor separado por virgula em 5 variaveis
  voos.setdefault((origem, destino), []) # adicionamos as chaves do dicionario e para cada chave é criada uma lista vazia
  voos[(origem, destino)].append((saida, chegada, int(preco))) # para cada chave adicono os respetivos voos
  

def imprimir_voos(agenda):
    id_voo = -1 #posição inicial invalida
    total_preco = 0
    #o vetor tem 12 posições, mas apenas são 6 voos, pois para cada passageiro terá o voo de ida e o outro de volta
    for i in range(len(agenda) // 2): # divisão do tamanho do vetor por 2, usasse 2 barras quando queremos garantir que a divisão resultará num valor inteiro
        cidade = local_pessoas[i][0] #cada localização guarda o nome da cidade
        aeroporto_orig = local_pessoas[i][1]
        id_voo += 1 #será a posição no vetor agenda referente aos voos de ida
        voo_ida = voos[(aeroporto_orig, destino)][agenda[id_voo]]
        id_voo +=1 #será a posição no vector agenda referente aos voos de volta
        voo_volta = voos[(destino, aeroporto_orig)][agenda[id_voo]]
        total_preco += voo_ida[2] + voo_volta[2] #posição 2 indica o preço do voo
        print('%10s%10s %6s-%5s %4s€ %6s-%5s %4s€' % 
            (cidade, aeroporto_orig, voo_ida[0], voo_ida[1], voo_ida[2],
            voo_volta[0], voo_volta[1], voo_volta[2]))

    print("Preço Total:", total_preco)
    
    
agenda = [1,2, 3,2, 7,3, 6,3, 2,4, 5,3] # vetor agrupado em 2 (ida e volta para cada passageiro)

#imprimir_voos(agenda)


################ Fitness Function #################
def fitness_function(agenda):
    id_voo = -1 #posição inicial invalida
    total_preco = 0
    #o vetor tem 12 posições, mas apenas são 6 voos, pois para cada passageiro terá o voo de ida e o outro de volta
    for i in range(len(agenda) // 2): # divisão do tamanho do vetor por 2, usasse 2 barras quando queremos garantir que a divisão resultará num valor inteiro
        aeroporto_orig = local_pessoas[i][1]
        id_voo += 1 #será a posição no vetor agenda referente aos voos de ida
        voo_ida = voos[(aeroporto_orig, destino)][agenda[id_voo]]
        id_voo +=1 #será a posição no vector agenda referente aos voos de volta
        voo_volta = voos[(destino, aeroporto_orig)][agenda[id_voo]]
        total_preco += voo_ida[2] + voo_volta[2] #posição 2 indica o preço do voo
    return total_preco


#agenda = [1,2, 3,2, 7,3, 6,3, 2,4, 5,3] # vetor agrupado em 2 (ida e volta para cada passageiro)
#print(fitness_function(agenda))



###### Uso da Biblioteca Mlrose que já contém algoritmos de otimização prontos a usar #######
# (https://mlrose.readthedocs.io/en/stable/source/intro.html)

fitness_func = mlrose.CustomFitness(fitness_function)
problem = mlrose.DiscreteOpt(length=12, # qtd de voos (6 ida, 6 volta)
                             fitness_fn=fitness_func, # função fitness personalizada
                             maximize=False, # é pretendido o minimo custo e nao o maximo
                             max_val=10) # cada viagem tem no máximo 10 voos disponiveis (gera nº de 0 a 9)




########################### Algoritmo Hill Climb ###########################

melhor_solucao, melhor_custo = mlrose.hill_climb(problem)

#print('Melhor solução', melhor_solucao)
#print('Melhor custo', melhor_custo)

#print('Algoritmo Hill Climb')
#imprimir_voos(melhor_solucao)



########################### Algoritmo Simulated Annealing ###########################
# Algoritmo baseado na física
# Annealing é o processo de aquecer um metal para o moldar
# Inicia uma solução aleatória utilizando uma variavel dada
# A cada estado é alterado apenas um valor de forma aleatória e compara o custo com o estado anterior
# no entanto caso a solução do novo estado seja pior que a do anterior, ele não descarta-a, 
# pois a seguir a uma solução pior, pode estar uma solução muito melhor que a primeira

melhor_solucao, melhor_custo = mlrose.simulated_annealing(problem, 
                                                          #schedule=mlrose.ArithDecay(), #metodos de otimização e parametros que permitem afinar o algoritmo
                                                          schedule=mlrose.GeomDecay(init_temp=10000),
                                                          #schedule=mlrose.ExpDecay()
                                                          random_state=1 #irá sempre apresentar o mesmo valor para todas as execuções, caso contrario ele irá proceder a um novo processo random
                                                          )
#print('Algoritmo Simulated Annealing')
# imprimir_voos(melhor_solucao)




########################### Algoritmo Genético ###########################
# Algoritmo mais popular que os anteriores e que apresenta geralmente melhores resultados
# Utiliza vetores para representar computacionalmente um "cromossoma"
# Gene é cada valor do vetor/cromossoma
# 1º - Inicia com uma poupulação inicial (definida pelo utilizador)
# 2º - Avaliação da população
# 3º - Decisão se a solução é considerada boa
# 4º - Caso não, poderá utilizar uma das seguintes técnicas de reajuste:
#    - Torneio: 
#    - Roleta: 
# 5º - Processo de reprodução através de:
#    - Crossover: 
#    - Mutação:

print('Algoritmo Genético')
melhor_solucao, melhor_custo = mlrose.genetic_alg(problem, 
                                                  pop_size=500, 
                                                  mutation_prob=0.2 #20% probabilidade de acontecer mutação
                                                  )
imprimir_voos(melhor_solucao)