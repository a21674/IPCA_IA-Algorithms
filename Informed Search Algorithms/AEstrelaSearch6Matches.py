# Jogo Puzzle do Fósforos
# Estado: Matriz 2x3
# Estado Inicial: 6 fósforos no índice [0][0]
# Estado Final: 1 fósforo em cada índice da matriz
# Modelo de Transição: a cada ação, um novo estado é gerado
# Ações/Regras: - Apenas é possivel mover um fósforo para a direita
#               - Mover 2 fósforos para a esquerda
#               - Mover 2 ou 3 fósforos para cim ou para baixo 

import numpy as np
from collections import OrderedDict

# Definição do estado, do estado inicial e do estado final
class Tabuleiro:
    def __init__(self, rows, columns, pieces) -> None:
        self.rows = rows
        self.columns = columns
        self.pieces = pieces
        self.vertice_inicial = []
        self.vertice_objetivo = []
        
    def set_vertice_inicial(self):
        self.vertice_inicial =  np.zeros((self.rows, self.columns), dtype = np.int)
        self.vertice_inicial[0][0] = self.pieces
        return self.vertice_inicial
    
    def set_vertice_objetivo(self):
        self.vertice_objetivo = np.ones((self.rows, self.columns), dtype = np.int)
        return self.vertice_objetivo
        
    def set_novo_estado(self):
        
        return
        
    def print_tabuleiro(self, vertice):        
        for row in vertice.estado:
            print(*row)
     
    
#Responsvel por criar um vertice (tabuleiro num determinado estado)
class Vertice:
    def __init__(self, estado) -> None:
        self.estado = estado
        self.heuristica = 0
        self.visitado = False
        self.vertices_adjacentes = []
        
    def adiciona_adjacente(self, adjacente):
        self.vertices_adjacentes.append(adjacente)
                
    # Heuristica (professor) definida pelo somatório dos valores ao quadrado, isso fará com que indices com muitas peças sejam + penalizados
    """ def calc_heuristica(self):        
        for i in range(len(self.estado)): #linhas
            for j in range(len(self.estado[i])): #colunas
                self.heuristica += self.estado[i][j]**2 """
    
    #Heuristica (sergio) definida pelo somatório de indices vazios
    def calc_heuristica(self):        
        for i in range(len(self.estado)): #linhas
            for j in range(len(self.estado[i])): #colunas
                if(self.estado[i][j] == 0):
                    self.heuristica += 1
    
 
    
# Responsavel por criar os vertices adjacentes a um vertice
class Adjacente:
    def __init__(self, vertice, custo = 1) -> None:
        self.vertice = vertice
        self.custo = custo #definido o custo de 1, irá armazenar o acumulado do custo até ao estado atual
        self.funcao_custo = vertice.heuristica + self.custo
   


# Função que implementa a busca A* 
class AEstrelaSearch:
    def __init__(self) -> None:
        self.cost = 1
        self.totalCost = 0
        self.finalizado = False        
        self.id_vertice_gerado = 0
        self.nivel_profundidade = 0
        self.percurso = []
            
    def print_percurso(self):
        i = 0
        for vertice in self.percurso:
            print("Estado {}".format(i))
            i += 1
            for row in vertice.estado:
                print(*row)
           
   
    def define_adjacentes(self, vertice_atual):       
        self.nivel_profundidade += 1 # desce um nivel 
        for i in range(len(vertice_atual.estado)): #linhas
            for j in range(len(vertice_atual.estado[i])): #colunas
                if vertice_atual.estado[i][j] > 0: #verifica se tem fosforos para mudar
                    
                    # Movimento para a direita
                    if j + 1 < len(vertice_atual.estado[i]) and vertice_atual.estado[i][j] > 0: #se tiver mais uma coluna ao lado direito
                        novo_estado = vertice_atual.estado.copy() #coloco aqui, pq irá ser necessário criar um novo estado para cada if
                        novo_estado[i][j] = novo_estado[i][j] - 1 #removido um fosforo do indice atual
                        novo_estado[i][j + 1] = novo_estado[i][j + 1] + 1 #adicionado um fosforo ao indice da coluna seguinte
                                                
                        novo_vertice = Vertice(novo_estado)
                        novo_vertice.calc_heuristica()
                        
                        vertice_atual.adiciona_adjacente(Adjacente(novo_vertice))
                                                           
                    # Movimento 2 fosforos para a esquerda
                    if j - 1 > 0 and vertice_atual.estado[i][j] > 1: #verificar se não está na primeira coluna para poder deslocar para a esquerda
                        novo_estado = vertice_atual.estado.copy() #coloco aqui, pq irá ser necessário criar um novo estado para cada if
                        novo_estado[i][j] = novo_estado[i][j] - 2 #removido 2 fosforos do indice atual
                        novo_estado[i][j - 1] = novo_estado[i][j - 1] + 2 #adicionado um fosforo ao indice da coluna seguinte
                                                
                        novo_vertice = Vertice(novo_estado)
                        novo_vertice.calc_heuristica()

                        vertice_atual.adiciona_adjacente(Adjacente(novo_vertice))
                        
                    # Movimento 2 ou 3 fosforos para cima
                    if i - 1 >= 0 and vertice_atual.estado[i][j] > 0: #verificar se não está na primeira linha para poder deslocar para cima
                        qtd_atual = 2 # forma de controlar a qtd de fosforos que o elemento tem, caso so tenha 1 irá apenas correr um ciclo
                        if vertice_atual.estado[i][j] > 2:
                            qtd_atual = 4
                        for qtd in range(2, qtd_atual): # para criar o estado tanto para 1 fosforo como 2 fosforos movimentados (3 não conta)
                            novo_estado = vertice_atual.estado.copy() #coloco aqui, pq irá ser necessário criar um novo estado para cada if
                            novo_estado[i][j] = novo_estado[i][j] - qtd #removido um fosforo do indice atual
                            novo_estado[i - 1][j] = novo_estado[i - 1][j] + qtd #adicionado um fosforo ao indice da linha anterior
                                                    
                            novo_vertice = Vertice(novo_estado)
                            novo_vertice.calc_heuristica()

                            vertice_atual.adiciona_adjacente(Adjacente(novo_vertice))
                            
                    # Movimento 2 ou 3 fosforos para baixo
                    if i + 1 < len(vertice_atual.estado) and vertice_atual.estado[i][j] > 0: #verificar se não está na última linha para poder deslocar para baixo
                        qtd_atual = 2 # forma de controlar a qtd de fosforos que o elemento tem, caso so tenha 2 irá apenas correr um ciclo (tendo em conta que para baixo so pode ser movido 2 ou 3 fosforos)
                        
                        #Se a posição atual tiver mais do que 2 fosforo, então ele pode fazer o ciclo para 2 fosforo, como para 3 fosforos
                        if vertice_atual.estado[i][j] > 2:
                            qtd_atual = 4
                        
                        for qtd in range(2, qtd_atual): # para criar o estado tanto para 1 fosforo como 2 fosforos movimentados (3 não conta)
                            novo_estado = vertice_atual.estado.copy() #coloco aqui, pq irá ser necessário criar um novo estado para cada if
                            novo_estado[i][j] = novo_estado[i][j] - qtd #removido um fosforo do indice atual
                            novo_estado[i + 1][j] = novo_estado[i + 1][j] + qtd #adicionado um fosforo ao indice da linha seguinte
                                                    
                            novo_vertice = Vertice(novo_estado)
                            novo_vertice.calc_heuristica()

                            vertice_atual.adiciona_adjacente(Adjacente(novo_vertice)) 
        return  
              
    def get_adjacente_menor_custo(self, adjacentes):
        adjacentes.sort(key=lambda x: x.funcao_custo)
        return adjacentes[0]
        
        
    def iniciar_busca(self, vertice_atual, vertice_objetivo):
        # 1 - Define o estado como já visitado
        vertice_atual.visitado = True
        self.percurso.append(vertice_atual)
        self.print_percurso()
        
        # 2 - Efetua teste objetivo
        if(np.array_equal(vertice_atual.estado, vertice_objetivo.estado)):
            self.finalizado = True
            self.totalCost += vertice_atual.heuristica
            print("Terminou com um custo total de: ", self.totalCost)
            return
        else:
        # 3 - Gera os estados possiveis a partir do estado atual
            self.define_adjacentes(vertice_atual)
            if vertice_atual.vertices_adjacentes:
                proximo_vertice = self.get_adjacente_menor_custo(vertice_atual.vertices_adjacentes)
                self.totalCost += proximo_vertice.custo          
                self.iniciar_busca(proximo_vertice.vertice, vertice_objetivo)





def main():
    newGame = Tabuleiro(2, 3, 6)
    
    vertice_inicial = Vertice(newGame.set_vertice_inicial())
    vertice_objetivo = Vertice(newGame.set_vertice_objetivo())
    
    print("Estado Inicial: ")
    newGame.print_tabuleiro(vertice_inicial)
    print("\nEstado Final: ")
    newGame.print_tabuleiro(vertice_objetivo)

    
    #inicio da busca
    print('\nInicio da Busca')
    start_search = AEstrelaSearch() #instanciamos a busca dando a cidade objectivo
    start_search.iniciar_busca(vertice_inicial, vertice_objetivo)
    
    
if __name__ == "__main__":
    main()