class vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):# 重载加法
        return vector(self.x+other.x,self.y+other.y)
    def __str__(self):
        return f"({self.x},{self.y})"
    
A=vector(1,2)
B=vector(3,4)
print(A+B)