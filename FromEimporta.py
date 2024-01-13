class SomarEMultiplicar():
    def __init__(self, numero1, numero2):
        self.somar = numero1 + numero2
        self.multiplicar = self.somar * 2
    def __str__(self):
        return f'Soma: {self.somar}, Multiplicação: {self.multiplicar}'