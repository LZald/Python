
class Vehiculo:

    def __init__(self, marca):
        self.marca = marca
    
    def mover(self):
        print(f"Moviendo el vehículo {self.marca}")

class Coche(Vehiculo):

    def __init__(self, marca, modelo, color="Negro"):
        super().__init__(marca)
        self.modelo = modelo
        self.color = color
        self.caract = []

    def export(self):
        str = ''
        for val in self.caract:
            str+=f';{val}'
        return f'{self.marca};{self.modelo};{self.color}{str}'

    def __str__(self):      ## def __repr__(self) -> str:
        str = ''
        for val in self.caract:
            str+=f' {val}'
        return f'{self.marca} {self.modelo} {self.color}{str}'

    def __repr__(self):
        return self.__str__()