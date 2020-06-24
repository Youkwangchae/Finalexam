import math
class Point:
    __x=0
    __y=0
    def __init__(self,a,b):
        self.__x = a
        self.__y = b
    def distance(self,other):
        length = 0
        x_length = 0
        y_length = 0
        x_length = (other.__x-self.__x)**2
        y_length = (other.__y-self.__y)**2
        length = math.sqrt(x_length+y_length)
        return length
    def __add__(self,other):
        self.__x = self.__x+other.__x
        self.__y = self.__y+other.__y
        p3 = Point(self.__x,self.__y)
        print("(",p3.__x,",",p3.__y,")")
        

p1 = Point(1,1)
p2 = Point(2,2)
print(p1.distance(p2))
p1+p2
