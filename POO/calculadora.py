class Calculadora:
#atributos
    numero1 = None
    numero2 = None
#contructor
    def __init__(self, n1=0, n2=0):
        self.numero1 = n1
        self.numero2 = n2
#metodos
    def sumar(self):
        return self.numero1 + self.numero2
    
    def restar(self):
        return self.numero1 - self.numero2
    
    def multplicacion(self):
        return self.numero1 * self.numero2
    
    def division(self):
        return self.numero1 / self.numero2
    
class CalculadoraCientifica(Calculadora):
    def __init__(self, n1, n2):
        super().__init__(n1, n2)

    def factorial(self, num):
        if(num <= 1):
            return 1
        else:
            return num * self.factorial(num -1)



if __name__ == "__main__" :
    casio = Calculadora()
    casio.numero1 = 10
    casio.numero2 = 5
    print(f"La Suma de 10 + 5 es : {casio.sumar()}")
    print(f"La resta de 10 - 5 es : {casio.restar()}")
    print(f"La multiplicacion de 10 * 5 es : {casio.multplicacion()}")
    print(f"La division de 10 / 5 es : {casio.division()}")

    hp = CalculadoraCientifica(20,8)
    print(f"La Suma con CC de ... es {hp.sumar()}")
    print(f"Factorial de 5:  {hp.factorial(5)}")