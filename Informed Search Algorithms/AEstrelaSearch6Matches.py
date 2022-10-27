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
        self.vertices_adjacentes = OrderedDict()
        
    def adiciona_adjacente(self, adjacente):
        self.vertices_adjacentes[adjacente.funcao_custo] = adjacente
    
    def calc_heuristica(self):        
        for i in range(len(self.estado)): #linhas
            for j in range(len(self.estado[i])): #colunas
                self.heuristica += self.estado[i][j]**2
            
    
# Responsavel por criar os vertices adjacentes a um vertice
class Adjacente:
    def __init__(self, vertice, custo = 1) -> None:
        self.vertice = vertice
        self.custo = custo
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
                    if i - 1 > 0 and vertice_atual.estado[i][j] > 0: #verificar se não está na primeira linha para poder deslocar para cima
                        qtd_atual = 2 # forma de controlar a qtd de fosforos que o elemento tem, caso so tenha 1 irá apenas correr um ciclo
                        if vertice_atual.estado[i][j] > 1:
                            qtd_atual = 3
                        for qtd in range(1, qtd_atual): # para criar o estado tanto para 1 fosforo como 2 fosforos movimentados (3 não conta)
                            novo_estado = vertice_atual.estado.copy() #coloco aqui, pq irá ser necessário criar um novo estado para cada if
                            novo_estado[i][j] = novo_estado[i][j] - qtd #removido um fosforo do indice atual
                            novo_estado[i - 1][j] = novo_estado[i - 1][j] + qtd #adicionado um fosforo ao indice da linha anterior
                                                    
                            novo_vertice = Vertice(novo_estado)
                            novo_vertice.calc_heuristica()

                            vertice_atual.adiciona_adjacente(Adjacente(novo_vertice))
                            
                    # Movimento 2 ou 3 fosforos para baixo
                    if i + 1 < len(vertice_atual.estado) and vertice_atual.estado[i][j] > 0: #verificar se não está na última linha para poder deslocar para baixo
                        qtd_atual = 2 # forma de controlar a qtd de fosforos que o elemento tem, caso so tenha 1 irá apenas correr um ciclo
                        if vertice_atual.estado[i][j] > 1:
                            qtd_atual = 3
                        for qtd in range(1, qtd_atual): # para criar o estado tanto para 1 fosforo como 2 fosforos movimentados (3 não conta)
                            novo_estado = vertice_atual.estado.copy() #coloco aqui, pq irá ser necessário criar um novo estado para cada if
                            novo_estado[i][j] = novo_estado[i][j] - qtd #removido um fosforo do indice atual
                            novo_estado[i + 1][j] = novo_estado[i + 1][j] + qtd #adicionado um fosforo ao indice da linha seguinte
                                                    
                            novo_vertice = Vertice(novo_estado)
                            novo_vertice.calc_heuristica()

                            vertice_atual.adiciona_adjacente(Adjacente(novo_vertice))
                
        return  
            
            
            
    def iniciar_busca(self, vertice_atual, vertice_objetivo):
        # 1 - Define o estado como já visitado
        vertice_atual.visitado = True
        self.percurso.append(vertice_atual)
        self.print_percurso()
        
        # 2 - Efetua teste objetivo
        if(np.array_equal(vertice_atual, vertice_objetivo)):
            self.finalizado = True
            print("Terminou com um custo total de: ", self.totalCost)
        else:
            self.define_adjacentes(vertice_atual)
            if vertice_atual.vertices_adjacentes:
                proximo_vertice = list(vertice_atual.vertices_adjacentes.values())[0]
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