import random

class ChutarNumero:
#parâmetros iniciais
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_min = 1
        self.valor_max = 100 
        self.tentar_novamente = True

    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        while self.tentar_novamente == True:
            if int(self.valor_do_chute) > self.valor_aleatorio:
                print("Chute um valor mais baixo")
                self.PedirValorAleatorio()
            elif int(self.valor_do_chute) < self.valor_aleatorio:
                print("Chute um valor mais alto")
                self.PedirValorAleatorio()
            self.tentar_novamente = False
            print("Parabéns, você acertou!")
            
#função para receber o chute do número
    def PedirValorAleatorio(self):
        self.valor_do_chute = input("Chute um número: ")
        
#função para gerar o valor aleatório entre o número mínimo e número máximo especificado no def init
    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_min, self.valor_max)

chute = ChutarNumero()
chute.Iniciar()
