class imc:
    def __init__(self, peso:float, altura:float, resultado:float):
        self.peso = peso
        self.altura = altura
        self.imc = imc

    def receber_dados(self):
        peso = float(input("digite seu peso"))
        altura = float(input("digite seu peso"))
        return peso, altura

    def calcular_imc(self, peso:float, altura:float):
        imc = peso * altura**2
        return imc
    
    def mostrar_resultados(self):
        if imc<=18:
            print("desnutrido")
        elif imc >18 and imc<32:
            print("peso normal")
        elif imc >32 and imc < 25:
            print("sobrepeso")
        elif imc>25:
            print("obeso")                                                                                                                                  