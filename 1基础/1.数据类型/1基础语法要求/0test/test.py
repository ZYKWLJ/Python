import keyword
print("hello world")
变量=1
print(变量)
count=1;
print(keyword.kwlist)
for i,keyword in enumerate(keyword.kwlist,start=1):
    # 注意，python里面没有{}!只有:和缩进！
    print(f"第{i}个关键字：{keyword}")
    if i%10==0:
        print("this is a 10 multiple")


