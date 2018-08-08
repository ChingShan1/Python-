dic10={}
dic11={'Taipei':'101','KingBoy':'me'}
print(dic11)

#加入項目
dic11['QeeenGirl']='you'
print(dic11)

#Use Loop print in dictionary of value
for key in dic11:
	print('%s: %s' %(key,dic11[key]))
#Delete the item of dictionary:use 'del'
del dic11['Taipei']
print(dic11)

#Get the index of dictionary:use '.keys()'
print(dic11.keys())
#Get the value of dictionary:use '.values()'
print(dic11.values())

#Get the document of the dictionary:use '.items()'
print(dic11.items())
print(tuple(dic11.items()))
#use '.get()' get value
print(dic11.get('KingBoy'))

#use '.pop()':刪除某一項鍵值
#use '.popitem()':刪除最後一項項鍵值
#use '.clear()':刪除辭典中所有項目
dic11.pop('QeeenGirl')
print(dic11)

dic11.popitem() 
print(dic11)

dic11.clear()

#use '.copy()':將某辭典 複製 另一個辭典
#use '.update()':將兩個辭典合併

dicA={1:'red',2:'green',3:'yellow'}
dicB={4:'black',5:'red'}
dicC=dicA.copy()
print(dicC)
#如果有相同鍵值，則只取一個鍵值
dicC.update(dicB)
print(dicC)


