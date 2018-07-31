def printstar(n):
	for i in range(1,n+1):
		print ('*',end = '')
	print()
def main():
	printstar(20)
	printstar(30)
	printstar(40)
main()
''''...........CUT(沒有參數和傳回值)...............'''
def total():
	sum=0
	for i in range(1,101):
		 sum+=i
	return sum

def main():
	t= total()
	print('summation of 1 to 100:',t)
main()
'''..........CUT(帶有參數和傳回值)................'''
def total2(a,b):
	sum=0
	for i in range(a,b+1):
		sum +=i
	return sum
def main():

	x=1
	y=10
	t=total2(x,y)
	print('summation of %d to %d : %d '%(x,y,t))

main()
'''..........CUT(回傳多個值)................'''
def test12(a,b):
	total=0
	avrage=0
	for i in range(a,b+1):
		total+=i
	avrage=total/(b-a+1)
	return total,avrage
def main():
	s, a= test12(1,100)
	print('sum = %d,avrage = %d '%(s,a))
main()
'''..........CUT(預設參數值)................'''
   #如果只給a參數值，漏掉b的參數值，補救方式:先給b預設值#
def test12(a,b=100):
	total=0
	avrage=0
	for i in range(a,b+1):
		total+=i
	avrage=total/(b-a+1)
	return total,avrage
def main():
	s, a= test12(1)
	print('sum = %d,avrage = %d '%(s,a))
	s, a= test12(1,10)
main()