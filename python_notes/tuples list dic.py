#coding = utf-8

#lists
lists = [0,1,1,0,[12,13],"a",(1,6),{"w":12,"e":33}]
#打印
print (lists[2])
print (lists[4])
print (lists)
print (lists[5])

#增加到最后一个
lists.append("zh")
print (lists)

#指定位置插入
lists.insert(3,"q")
print (lists)

#删除值为1的第一个元素
lists.remove(1)
print (lists)

#删除指定位置的元素，并返回
lists.pop(0)
print (lists)

#返回列表中第一个为1的元素索引
m=lists.index(1)
print (m)

#计算1出现的次数
n=lists.count(1)
print (n)

#正向排序
listsa=[1,0,3]
listsa.sort()
print (listsa)

#方向排序
listsa.reverse()
print (listsa)

#lists作为堆栈，先入后出
listsb=[1,4,8]
listsb.append(9)
print (listsb)
listsb.pop()
print (listsb)

#del删除指定索引的子项
del listsb[0]
print (listsb)




#元组

print (u"元组开始")

tuples = (0,1,1,0,[12,13],"a",(1,6),{"w":12,"e":33})
#打印
print (tuples[2])
print (tuples[4])
print (tuples)
print (tuples[5])

#返回列表中第一个为1的元素索引
m=tuples.index(1)
print (m)

#计算1出现的次数
n=tuples.count(1)
print (n)


#集合,不重复的数据

print (u"集合开始")
sets = [1,1,2,3,4,2]
s = set(sets)
print (s)





#字典
print (u"字典开始")
dic = {"a":1,"b":2,"c":3}

#查值
a=dic["a"]
print (a)

#添加
dic["d"]=4
print(dic)

#删除
del dic["a"]
print (dic)



