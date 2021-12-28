# una funcion que esta dentro de una clase que determina una accion o comportamiento

class Matematica():
    def suma(self):
        self.n1 = 2 #variables del metodo
        self.n2 = 3 #variables del metodo

s = Matematica()
s.suma()
print(s.n1 + s.n2)

# __init__ es un contructor

class Ropa():
    def __init__(self):
        self.marca = "willow"
        self.talla = "m"
        self.color = "rojo"

camisa = Ropa()
print(camisa.talla)
print(camisa.color)

#another example with variables

class Calculadora:
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2
        self.producto = n1 * n2
        self.division = n1 / n2


operacion = Calculadora(10,3)
print(operacion.suma    )