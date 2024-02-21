class Punto:
    def ___init__(self, coordenada_x, coordenada_y):
        self.coordenada_x = coordenada_x
        self.coordenada_y = coordenada_y
    
    def mostrar(self,imprimir):
        self.imprimir = imprimir
        
        imprimir = print(self.coordenada_x,self.coordenada_y)
    
    def mover(self, ncoordenada_x, ncoordenada_y):
        self.ncoordenada_x = ncoordenada_x
        self.ncoordenada_y = ncoordenada_y
        
        self.coordenada_x = ncoordenada_x
        self.coordenada_y = ncoordenada_y
        
    def calcular_distancia(self, punto_nuevo_X, punto_nuevo_y, x, t):
        self.punto_nuevo_x = punto_nuevo_X
        self.punto_nuevo_y = punto_nuevo_y
        self.x = x
        self.y = y
        
        if self.coordenada_x < punto_nuevo_X:
            x = punto_nuevo_X-self.coordenada_x
        if self.coordenada_x > punto_nuevo_X:
            x = self.coordenada_x - punto_nuevo_X
        if self.coordenada_x == punto_nuevo_X:
            x = 0
        if self.coordenada_y < punto_nuevo_y:
            y = punto_nuevo_y - self.coordenada_y
        if self.coordenada_y > punto_nuevo_X:
            y = self.coordenada_y - punto_nuevo_y
        if self.coordenada_y == punto_nuevo_y:
            y = 0                  
        
    
        
            