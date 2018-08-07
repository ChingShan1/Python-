#數組的元素不可改變
#串列(list)與tuple。串列與tuple非常類似，唯一的差別在於: 串列可以修改，而tuple不能修改。
#沒有提供append insert，但可以利用+來加入元素或利用*來複製元素
tuple1=(1,2,3,4,5)
print(tuple1)
#由串列中建立數組
tuple2=tuple([x for x in range(1,8)])
list1=list([x for x in range(1,8)])
print(list1)
print(tuple2)

tuple3=tuple('Python')
print(tuple3)

tuple1 +=(6,)
print(tuple1)

#可利用del刪除整個數組
del tuple3