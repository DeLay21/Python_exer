class jogador:
    def __init__(self, nome, pontuacao= 0):
        self.nome = nome
        self.pontuacao = pontuacao

    def pontuar(self, ponto= 1):
        self.pontuacao += ponto
    
    def mostrar_pontos(self):
        print(f"O jogador {self.nome} tem {self.pontuacao}")

jogador1 = jogador("Isaac")
jogador2 = jogador("arthur")

jogador1.pontuar(2)
jogador2.pontuar(3)


jogador1.mostrar_pontos()
jogador2.mostrar_pontos()
