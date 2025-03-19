b=b'123abc'
print(b[1:2])
for i in b:
    print(i)
    
# bytes() 函数用于创建一个新的不可变字节对象，它接受的参数必须是一个可迭代对象，
# 且该可迭代对象中的元素必须是 0 到 255 之间的整数。
s={1,2,3};
b1=bytes(s)
print(b1)
for i in b1:
    print(i)