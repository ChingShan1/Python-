import pickle
#variable_name=open('file_name','mode')
#variable_name:表示使用自訂的變數名稱
#file_name:是使用者自訂檔案名稱
'''mode:是檔案運作的屬性
	-----文字檔模式-----
		w:寫入
		r:讀取
		a:附加
	-----二進制模式-----
		wb:寫入
		rb:讀取
		ab:附加      
'''

outfile=open('names.dat','w')
with open('names1.dat','w') as outfile :
	outfile.write('apple\n')
	outfile.write('orange\n')
	outfile.write('grapr\n')
	outfile.close()

'''-------------------
	 read()=readlines():讀取檔案所有內容
	 readline():從檔案讀取一行
	 read(num):從檔案中讀取num個字元
'''
with open('names1.dat','r') as test1_file:
	data1=test1_file.read()
	print(data1)
	test1_file.close()
with open('names1.dat','r') as test2_file:
	data2=test2_file.readline()
	print(data2)
	test2_file.close()

'''-----重要--------
	只要在檔案的模式中加入+，就直接處理讀入和讀寫的動作，不用多寫 .close() 這段
'''
with open('names1.dat','r+') as test1_file:
	data1=test1_file.read()
	print(data1)
with open('names1.dat','r+') as test2_file:
	data2=test2_file.readline()
	print(data2)

#如果純數值的話，二進制比要有效率，使用pickle模組
'''-----二進制檔案-------
	pickle.dump():寫入
	pickle.load():讀取
'''
with open('binaryfile.dat','wb') as bfile:
	pickle.dump(123,bfile)
	bfile.close()

with open('binaryfile.dat','rb') as bfile:
	data=pickle.load(bfile)
	print(data)
	bfile.close()

'''例外處理 
	try:
	
	except < T > :

	except:

	else:

	finally:
'''
