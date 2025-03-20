#!/usr/bin/python3
 
class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return 'hello world'
 
# 实例化类
x = MyClass()
 
# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())

def g(name):# 从这里也能看出，函数也是对象,这就是python的一切皆对象特点！
    print("hello",name) 
    # print(__class__)
g("world")
print(type(g))# 输出<class 'function'>


class person:
    def __init__(self,name,age):
        print(self)# 输出<__main__.person object at 0x7ffb8fc3ee40>
        # Python 中一切都是对象，所有的类最终都继承自内置的 object 类。这里输出的是at 0x7ffb8fc3ee40，是指这个类实例在内存中位置
        print("_init_")
        print(__class__)
        print(type(self))#这里等价于type(person)
        self.name=name
        self.age=age
        pass # 相当于其他语言的TODO
    def say(self):
        print("my name is",self.name,"my age is",self.age)
        pass
A=person("A",18)
A.say()


# 打印一个类的内置属性
print(person.__doc__)
print(person.__name__)
print(person.__module__)