#循环


#字典
dic = {"a":1,"b":2}
for k,v in dic.items():
    print (k,v)


#序列 索引和对应值
lists =["a","b","c"]
for i,v in enumerate(lists):
    print (i,v)


#排序后循环
nums = [1,2,8,3,5,6,7]
for i in sorted(nums):
    print (i)
for i in reversed(nums):
    print (i)

#复制后循环副本
names =["zhang","suai","shh","cdd"]
for i in names[:]:
    if len(i)>3:
        print (i)
