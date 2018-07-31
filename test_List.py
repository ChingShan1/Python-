temp=[1,2,3.14,'apple']
print(temp)
print(temp[3])
'''len()計算串列長度'''
print(len(temp))
'''............cut..........'''
#.append(value) 將value加入串列尾端
#.insert(index,value) 將value 加入串列的索引為index處
temp.append(123)
print(temp)
temp.insert(0,'start')
print(temp)
'''............cut..........'''
#.pop()刪除串列的最後一項
#.pop(index)刪除串列的index處
#.remove(value) 刪除串列中有value值的項目，如果有重複value的項目，只刪除第一個出現的項目
temp.pop()
print(temp)
temp.pop(0)
print(temp)
temp.remove(3.14)
print(temp)
'''............cut..........'''
#.sort()將串列由小到大排序
#.reverse()將串列加以反轉
temp.append(24)
temp.remove('apple')
temp.sort()
print(temp)
temp.reverse()
print(temp)

