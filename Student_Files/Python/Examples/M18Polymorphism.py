class Shape:
    __x = None
    __y = None
    def __init__(self, x, y):       #constructor
        self.__x = x 
        self.__y = y
    def getX(self):                 #getters/accessors
        return self.__x
    def getY(self):
        return self.__y
    def setX(self, x):
        self.__x = x
    def setY(self, y):
        self.__y = y
    def draw(self):
        print("type=%s: draw in Shape called" % type(self))
    def __repr__(self):
        return "x={},y={}".format(self.__x,self.__y)
    
class Circle( Shape):
    __r= 1
    def __init__(self, x, y, r):
        #self.setX(x)     
        #self.setY(y)
        super().__init__(x,y) 
        self.__r = r
    def draw(self):
        print("type=%s: draw in Circle called" % type(self))
    def __repr__(self):
        return "x={},y={},r={}".format(self.getX(),self.getY(),self.__r)

class Rect( Shape):
    __width= None
    __height=None
    def __init__(self, x, y, width, height):
        self.setX(x)     
        self.setY(y) 
        self.__width = width
        self.__height = height
    def draw(self):
        print("---Rect does both parent and child draw()--")
        super().draw()
        print("type=%s: draw in Rect called" % type(self))
    def __repr__(self):
        return "x={},y={},width={},height={}".format(self.getX(),self.getY(),
                                                     self.__width, self.__height)
class Point( Shape):
    def __init__(self, x, y):
        self.setX(x)     
        self.setY(y) 

shapes = [ Shape( 23, 24),  Point(23, 24), Circle( 25, 26, 27),  
          Circle( 2, 6, 222), Rect(23, 12, 23 ,23)]
for s in shapes:
    s.draw()
    
print(dir(shapes[0]))
