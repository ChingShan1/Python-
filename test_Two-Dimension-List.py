import random
temp=[['1','2','3'],['4','5','6']]
print(temp)
print(temp[0])
print(temp[1][2])
'''..........cut..........'''
temp2=[]
row =3
column=5
for i in range(row):
	temp2.append([])
	for j in range(column):
		temp2[i].append(random.randint(1,20))
print(temp2)