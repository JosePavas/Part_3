#Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.
class Vehiculo:
    def __init__(self, velocidad_maxima, kilometraje) -> None:
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

v1 = Vehiculo(250,25000)
v2 = Vehiculo(180,48520)
print(v1.kilometraje, v1.velocidad_maxima, v2.kilometraje, v2.velocidad_maxima)
