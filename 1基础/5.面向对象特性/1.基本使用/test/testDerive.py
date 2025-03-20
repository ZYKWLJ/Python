# 继承的语法！
# class 派生类名(基类名)
class person:
    name : str
    age : int
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say(self):
        print("hey this is person, my name is",self.name,"my age is",self.age)

class student(person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade=grade
    def say(self):
        print("hey this is student, my name is",self.name,"my age is",self.age,"my grade is",self.grade)
A=student("A",18,1)
A.say()

super(student,A).say() # 子类调用父类的方法
