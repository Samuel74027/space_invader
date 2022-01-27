# naming conventions
ALL_CAPS = "Constent"

class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltax, deltay):
        self.x += deltax
        self.y += deltay
    def distance(self, new_x, new_y):
        x_sq = (self.new_x-self.x)**2
        y_sq = (self.new_y-self.y)**2
        return ((x_sq+y_sq)**0.5)
    
class Ship(Point):
    # global method
    fireRate = 3
    xShiftRate = 10
    yShiftRate = 20
    def __init__(self, x, y):
        super().__init__(x, y)
    def distance(self,new_x, new_y):
         super().distance(new_x, new_y)
    def start(self, something):
        return self.something
        
        
        

ship1 = Ship(10, 20)
ship1.distance(0, 0)

