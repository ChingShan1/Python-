set1={1,3,5}
set2=set()
set3=set([x for x in range(1,6)])
print(set3)

#集合不會包含重複資料
set4={1,1,1,2,3,4,4,5,5}
print(set4)

#add(x)將x加入集合中
#remove(x)將x從集合中刪除
set4.add(6)
print(set4)
set4.remove(2)
print(set4)

for x in set4:
	print(x,end=' ')
print()

#聯集
print(set1 | set4)
print(set1.union(set4))

#交集
print(set1 & set4)
print(set1.intersection(set4))

#差集:將A集合去掉與B集合共有項目
set5={1,6,8,10,20}
set6={1,3,8,10}
print(set5 - set6)
print(set5.difference(set6))
print(set6 - set5)

#對稱交集:去掉A集合與B集合共有的項目
print(set5 ^ set6)
print(set5.symmetric_difference(set6))

#subset 子集合:如果A集合的所有項目是B集合的部分集合 則稱A是B的部分集合，而B是A的超集合
#superset 超集合
set7={1,3,8,19}
set8={1,3,8}
print(set8.issubset(set7))
print(set7.issuperset(set8))

#== 和 !=
print(set7 == set8)
print(set7 != set8)
