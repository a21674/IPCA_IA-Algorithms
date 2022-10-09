######### A* Search - Arad to Bucarest Problem #########
# Este algoritmo de pesquisa usa para além da heuristica do caminho em linha recta, o custo do grafo, 
# ou seja a distancia em km de uma cidade às suas adjacentes para a decisão do melhor caminho

import numpy as np

class Vertice:
    def __init__(self, cidade, distancia_objectivo) -> None:
        self.cidade = cidade
        self.distancia_objectivo = distancia_objectivo
        self.visitado = False
        self.cidades_adjacentes = []
        
    def adiciona_adjacente(self, adjacente):
        self.cidades_adjacentes.append(adjacente)
        
        
    def mostra_cidades_adjacentes(self):
        for i in self.cidades_adjacentes:
            print(i.vertice.cidade, i.custo)
            

class Adjacente:
    def __init__(self, vertice, custo) -> None:
        self.vertice = vertice
        self.custo = custo
        self.distancia_aestrela = vertice.distancia_objectivo + self.custo
    
class Mapa_Grafo:
    #mapeamento das cidades/vertices e valor em linha reta ao objectivo (heuristica)
    arad = Vertice('Arad', 366)
    zerind = Vertice('Zerind', 374)
    oradea = Vertice('Oradea', 380)
    sibiu = Vertice('Sibiu', 253)
    timisoara = Vertice('Timisoara', 329)
    lugoj = Vertice('Lugoj', 244)
    mehadia = Vertice('Mehadia', 241)
    dobreta = Vertice('Dobreta', 242)
    craiova = Vertice('Craiova', 160)
    rimnicu = Vertice('Rimnicu', 193)
    fagaras = Vertice('Fagaras', 178)
    pitesti = Vertice('Pitesti', 98)
    bucharest = Vertice('Bucharest', 0)
    giurgiu = Vertice('Giurgiu', 77)

    #adicionar as cidades adjacentes com a distancia
    arad.adiciona_adjacente(Adjacente(zerind, 75))
    arad.adiciona_adjacente(Adjacente(sibiu, 140))
    arad.adiciona_adjacente(Adjacente(timisoara, 118))

    zerind.adiciona_adjacente(Adjacente(arad, 75))
    zerind.adiciona_adjacente(Adjacente(oradea, 71))

    oradea.adiciona_adjacente(Adjacente(zerind, 71))
    oradea.adiciona_adjacente(Adjacente(sibiu, 151))

    sibiu.adiciona_adjacente(Adjacente(oradea, 151))
    sibiu.adiciona_adjacente(Adjacente(arad, 140))
    sibiu.adiciona_adjacente(Adjacente(fagaras, 99))
    sibiu.adiciona_adjacente(Adjacente(rimnicu, 80))

    timisoara.adiciona_adjacente(Adjacente(arad, 118))
    timisoara.adiciona_adjacente(Adjacente(lugoj, 111))

    lugoj.adiciona_adjacente(Adjacente(timisoara, 111))
    lugoj.adiciona_adjacente(Adjacente(mehadia, 70))

    mehadia.adiciona_adjacente(Adjacente(lugoj, 70))
    mehadia.adiciona_adjacente(Adjacente(dobreta, 75))

    dobreta.adiciona_adjacente(Adjacente(mehadia, 75))
    dobreta.adiciona_adjacente(Adjacente(craiova, 120))

    craiova.adiciona_adjacente(Adjacente(dobreta, 120))
    craiova.adiciona_adjacente(Adjacente(pitesti, 138))
    craiova.adiciona_adjacente(Adjacente(rimnicu, 146))

    rimnicu.adiciona_adjacente(Adjacente(craiova, 146))
    rimnicu.adiciona_adjacente(Adjacente(sibiu, 80))
    rimnicu.adiciona_adjacente(Adjacente(pitesti, 97))

    fagaras.adiciona_adjacente(Adjacente(sibiu, 99))
    fagaras.adiciona_adjacente(Adjacente(bucharest, 211))

    pitesti.adiciona_adjacente(Adjacente(rimnicu, 97))
    pitesti.adiciona_adjacente(Adjacente(craiova, 138))
    pitesti.adiciona_adjacente(Adjacente(bucharest, 101))

    bucharest.adiciona_adjacente(Adjacente(fagaras, 211))
    bucharest.adiciona_adjacente(Adjacente(pitesti, 101))
    bucharest.adiciona_adjacente(Adjacente(giurgiu, 90))



class VetorOrdenado:    
    #Construtor
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1 #indicará que o array quando instanciada a class estará vazio
        self.valores = np.empty(self.capacidade, dtype=object) #array limpo com tamanho e tipo de dados
            
            
    #Irá inserir um objecto do tipo Vertice usando a distancia_aestrela como valor a ordenar 
    def insere_ordenado (self, adjacente):        
        # 1- Verifica se o vetor está cheio ou vazio
        if self.ultima_posicao == self.capacidade - 1: #verifica se o array já está cheio
            print("O vetor está cheio")
            return
        
        # 2 - procura da posição certa para inserir o novo valor
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i].distancia_aestrela > adjacente.distancia_aestrela: #compara o vertice do vetor com o recebido por parametro
                break
            if posicao == self.ultima_posicao: # caso o valor a inserir seja maior que todos os ja existentes, para que ele seja inserido na ultima posição
                posicao += 1
            
        # 3 - Desloca uma posição para a direita os valores superiores ao valor de entrada. Como temos acesso ao tamanho do array, começamos pela última posição
        pos = self.ultima_posicao #var de apoio que irá de forma decrescente da ultima posição até a posição que irá ser inserido
        while pos >= posicao:
            self.valores[pos + 1] = self.valores[pos] #vamos mover o valor da posição atual para o elemento seguinte
            pos -= 1 #decrementamos 1 até chegar á posição onde vamos inserir
        
        # 4 - Depois de movidos todos os valores para a direita, agora inserimos o valor vindo por parametro na posição ordenada
        self.valores[posicao] = adjacente
        self.ultima_posicao += 1 # atualizamos a ultima posição do array


    def imprime(self):
        if self.ultima_posicao == -1:
            print("Array está vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', 
                      self.valores[i].vertice.cidade, ' - ', 
                      self.valores[i].custo, ' - ',
                      self.valores[i].vertice.distancia_objectivo, ' - ', 
                      self.valores[i].distancia_aestrela 
                      )
        
        
        
class AEstrelaSearch:
    def __init__(self, objectivo) -> None:
        self.objectivo = objectivo
        self.encontrou = False
        
    def iniciar_busca(self, atual):
        print("---------")
        print('Atual {}'.format(atual.cidade))
        print('Pos - Cidade - Custo - Linha Reta - Distancia Estrela')
        atual.visitado = True
        
        if atual == self.objectivo: #testa sempre se o atual é o objectivo, mesmo no primeiro nó
            self.encontrou = True
        else:
            vetor_ordenado_adjacentes = VetorOrdenado(len(atual.cidades_adjacentes)) # cria um vetor ordenado para adicionar as cidades adjacentes da cidade atual, conforme forem visitadas
            for adjacente in atual.cidades_adjacentes:
                if adjacente.vertice.visitado == False:
                    adjacente.vertice.visitado = True
                    vetor_ordenado_adjacentes.insere_ordenado(adjacente)
                    
            vetor_ordenado_adjacentes.imprime()
            
            if vetor_ordenado_adjacentes.valores[0] != None: #verifica se o vetor esta vazio
                self.iniciar_busca(vetor_ordenado_adjacentes.valores[0].vertice) #chamada recursiva pela cidade que tem menos distancia_aestrela pois o vetor está ordenado por ordem crescente




def main():
    mapa = Mapa_Grafo()
    mapa.arad.mostra_cidades_adjacentes()


    #inicio da busca
    print('')
    print('Inicio da Busca')
    start_search = AEstrelaSearch(mapa.bucharest) #instanciamos a busca dando a cidade objectivo
    start_search.iniciar_busca(mapa.arad) # iniciamos a busca dando a cidade inicial
    
    
if __name__ == "__main__":
    main()