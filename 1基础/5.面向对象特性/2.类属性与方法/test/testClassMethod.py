class MyClass:
    def __init__(self, data):
        # 构造函数，在生成对象时调用
        self.data = data
        print("对象已创建")

    def __del__(self):
        # 析构函数，释放对象时使用
        print("对象已释放")

    def __repr__(self):
        # 打印，转换
        return f"MyClass({self.data})"

    def __setitem__(self, index, value):
        # 按照索引赋值
        self.data[index] = value

    def __getitem__(self, index):
        # 按照索引获取值
        return self.data[index]

    def __len__(self):
        # 获得长度
        return len(self.data)

    def __add__(self, other):
        # 加运算
        if isinstance(other, MyClass):
            return MyClass(self.data + other.data)
        return MyClass(self.data + other)

    def __sub__(self, other):
        # 减运算
        if isinstance(other, MyClass):
            return MyClass([a - b for a, b in zip(self.data, other.data)])
        return MyClass([a - other for a in self.data])

    def __mul__(self, other):
        # 乘运算
        if isinstance(other, MyClass):
            # 内置函数，用于将多个可迭代对象（如列表、元组、字符串等）中的元素一一对应地打包成一个个元组，
            # 然后返回一个由这些元组组成的迭代器。
            return MyClass([a * b for a, b in zip(self.data, other.data)])
        return MyClass([a * other for a in self.data])

    def __truediv__(self, other):
        # 除运算
        if isinstance(other, MyClass):
            return MyClass([a / b for a, b in zip(self.data, other.data)])
        return MyClass([a / other for a in self.data])

    def __mod__(self, other):
        # 求余运算
        if isinstance(other, MyClass):
            return MyClass([a % b for a, b in zip(self.data, other.data)])
        return MyClass([a % other for a in self.data])

    def __pow__(self, other):
        # 乘方
        if isinstance(other, MyClass):
            return MyClass([a ** b for a, b in zip(self.data, other.data)])
        return MyClass([a ** other for a in self.data])

    def __call__(self):
        # 函数调用
        print("对象被当作函数调用")
        return sum(self.data)


# 测试代码
if __name__ == "__main__":
    obj1 = MyClass([1, 2, 3])
    obj2 = MyClass([4, 5, 6])

    print(obj1)  # 调用 __repr__
    obj1[0] = 10  # 调用 __setitem__
    print(obj1[0])  # 调用 __getitem__
    print(len(obj1))  # 调用 __len__

    result_add = obj1 + obj2  # 调用 __add__
    print(result_add)

    result_sub = obj1 - obj2  # 调用 __sub__
    print(result_sub)

    result_mul = obj1 * obj2  # 调用 __mul__
    print(result_mul)

    result_div = obj1 / 2  # 调用 __truediv__
    print(result_div)

    result_mod = obj1 % 2  # 调用 __mod__
    print(result_mod)

    result_pow = obj1 ** 2  # 调用 __pow__
    print(result_pow)

    total = obj1()  # 调用 __call__
    print(total)    