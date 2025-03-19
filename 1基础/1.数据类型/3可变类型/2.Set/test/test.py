s={'1','2','3','3','a',2,'8',444}
if '1' in s:
    print('1 in set')
else :
    print('1 not in set')
# sorted(s)
for i in s:{# 乱序输出，且不重复。由内部哈希表实现输出顺序
    print(i)#自动换行
    # print(i,end='····')#不换行
}

set([1,2,3,4])
print(s)