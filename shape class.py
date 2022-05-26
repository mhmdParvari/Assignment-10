class Shape:
    def __init__(self):
        self.area=0
        self.perimeter=0
    
    def calcArea(self):
        pass
    def calcPerimeter(self):
        pass
    def printArea(self):
        print(self.area)
        
    def printPerimeter(self):
        print(self.perimeter)


class Circle(Shape):
    def __init__(self,radius):
        super().__init__()
        self.r=radius

    def calcArea(self):
        self.area=3.14*self.r**2
    
    def calcPerimeter(self):
        self.perimeter=3.14*self.r*2

    
class Rectangle(Shape):
    def __init__(self,length,width):
        super().__init__()
        self.l=length
        self.w=width

    def calcArea(self):
        self.area=self.l*self.w

    def calcPerimeter(self):
        self.perimeter=(self.l+self.w)*2
        
c=Circle(3)
c.calcArea()
c.calcPerimeter()
c.printArea()
c.printPerimeter()
r=Rectangle(2,5)
r.calcArea()
r.calcPerimeter()
r.printArea()
r.printPerimeter()