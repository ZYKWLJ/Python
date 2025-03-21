class Student:
    name: str
    __age: int # 年龄保密
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self): # 这个是内置方法，调用print时会自动调用之！
        return f"{self.name} is {self.age} years old"# 格式化字符串，嵌入表达式
    def say(self):
        print("hey this is student, my name is",self.name,"my age is",self.age)
A=Student("A",18)
print(A)
# A.say()
# A.__str() 私有方法无法访问
# print(A.name+A.age)私有属性无法访问