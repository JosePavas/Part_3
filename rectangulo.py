#Cree una clase Rectángulo la cual contiene dos atributos de instancia
#que representan los puntos que definen sus esquinas. 
#Agregue métodos a la clase Rectángulo para calcular su perímetro, 
#calcular su área e indicar si el rectángulo es un cuadrado.
class Rectangulo:
    
    def __init__(self, coordenada_x, coordenada_y) -> None:
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
        
    def rectas(self, recta_1, recta_2):
        self.recta_1 = recta_1
        self.recta_2 = recta_2
        pass
                