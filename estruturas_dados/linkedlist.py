class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):  # Construtor dos atributos
        self.head = None  # Referência para primeiro nó
        self.size = 0

    def append(self, data):
        new_node = Node(data)  # Cria um novo nó

        self.size += 1  # Adiciona o nó ao tamanho da lista

        if self.head == None:
            self.head = new_node  # Se não existir head ainda, torna o novo nó como a head
            return

        pointer = self.head  # O ponteiro se torna a head

        while pointer.next:
            pointer = pointer.next  # Se houver o campo next tiver valor, ele não para de percorrer os valores até achar um nó sem o endereço de um novo nó
        
        pointer.next = Node(data)# Agora que o pointer está na ultima posição, ele coloca a data no último nó. O novo elemento possui um next vazio



    def __len__(self):
        return self.size

    
    def __getitem__(self, index):
        #indentificar item  a = lista[5]

        pointer = self.head #Ponteiro vai para o head da lista
        for i in range(index):
            if pointer: # se tiver um pointer no index
                pointer = pointer.next #Avança para o próximo ponteiro
            else:
                raise IndexError("Não há esse índice no código") #Ex: código tem 4 elementos e o usuário pede o índice 25
            
        if pointer: #Ver se o índice não é vazio
            return pointer.data
        else: 
            raise IndexError("Não há esse índice no código") #Ex: código tem 3 elementos e o usuário pede o índice 3, o qual é vazio pois começa no 0


    def __setitem__(self, index, data):
        #trocar itens  lista[3] = 9

        pointer = self.head #Ponteiro vai para o head da lista
        for i in range(index):
            if pointer: # se tiver um pointer no index
                pointer = pointer.next #Avança para o próximo ponteiro
            else:
                raise IndexError("Não há esse índice no código") #Ex: código tem 4 elementos e o usuário pede o índice 25
            
        if pointer: #Ver se o índice não é vazio
            pointer.data = data
        else: 
            raise IndexError("Não há esse índice no código") #Ex: código tem 3 elementos e o usuário pede o índice 3, o qual é vazio pois começa no 0
        
    
    def search_index(self, elem):
        pointer = self.head
        i = 0 #posição
        while pointer:
            if pointer == elem: #Checar se o ponteiro é o elemento
                return i #Se sim retornar posição
            else:
                pointer = pointer.next #Se não, avançar pro próximo ponteiro e adicionar 1 no índice
                i += 1
        raise ValueError("Não há esse elemento na lista")
