#Cree una clase Circulo que tenga las propiedades centro y radio,
# las cuales se inicializan con parámetros en el constructor.
# Defina métodos en la clase para calcular el área, 
# el perímetro e indicar si un punto pertenece al círculo o no.

class Circulo:
    def __init__(self, centro_x, centro_y, radio) -> None:
        self.centro_x = centro_x
        self.centro_y = centro_y
        self.radio = radio
    
    def area (self, area_c):
        self.area_c = area_c
        area_c = 3.14 * (self.radio ** 2)
        print(area_c)
      
    def perimetro (self, perimetro_c):
        self.perimetro_c = perimetro_c
        perimetro_c = (3.14 * 2) * self.radio
    
    def punto_dentro_circulo (self, punto_a, punto_b):
        self.punto_a = punto_a
        self.punto_b = punto_b
        
        if (punto_a - self.centro_x) * 2 + (punto_b - self.centro_y) * 2 == self.radio:
            punto_a , punto_b is True        
        
            

