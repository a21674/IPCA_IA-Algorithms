import numpy as np

class VetorOrdenado:
    
    #Construtor
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1 #indicará que o array estará vazio
        self.valores = np.empty(self.capacidade, dtype=int) #array limpo com tamanho e tipo de dados
    
    
    def imprime(self):
        if self.ultima_posicao == -1:
            print("Array está vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])

    
    #processo que será em média de O(n/2), no pior caso O(n) se tiver que inserir na última posição 
    def insere_ordenado (self, valor):
        
        # 1- Verifica se o array está cheio ou vazio
        if self.ultima_posicao == self.capacidade - 1: #verifica se o array já está cheio
            print("O array está cheio")
            return
        
        # 2 - procura da posição certa para inserir o novo valor
        posicao = 0
        for i in range(self.ultima_posicao + 1):
            posicao = i
            if self.valores[i] > valor:
                break
            if posicao == self.ultima_posicao: # caso o valor a inserir seja maior que todos os ja existentes, para que ele seja inserido na ultima posição
                posicao += 1
            
        # 3 - Desloca uma posição para a direita os valores superiores ao valor de entrada. Como temos acesso ao tamanho do array, começamos pela última posição
        pos = self.ultima_posicao #var de apoio que irá de forma decrescente da ultima posição até a posição que irá ser inserido
        while pos >= posicao:
            self.valores[pos + 1] = self.valores[pos] #vamos mover o valor da posição atual para o elemento seguinte
            pos -= 1 #decrementamos 1 até chegar á posição onde vamos inserir
        
        # 4 - Depois de movidos todos os valores para a direita, agora inserimos o valor vindo por parametro na posição ordenada
        self.valores[posicao] = valor
        self.ultima_posicao += 1 # atualizamos a ultima posição do array
        



def main():
    vetor = VetorOrdenado(10)
    vetor.insere_ordenado(4)
    vetor.insere_ordenado(2)
    vetor.insere_ordenado(1)
    vetor.insere_ordenado(3)
    vetor.imprime()

if __name__ == "__main__":
    main()
