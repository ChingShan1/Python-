s1='Learning python now !'
print(s1)

print(s1[2])

print(s1[:4])

print(s1[4:])

#isalnum():如果字串的字元是由字母和數字所組成的話，則回傳True
#isalpha():如果字串的字元是由字母所組成的話，則回傳True
#isdigit():如果字串的字元是由數字所組成的話，則回傳True

print(s1.isalnum())
print(s1.isalpha())
print(s1.isdigit())

#endswith():如果字串的尾端是S1子字串時，則回傳true
#startswitch():如果字串的開頭是S1子字串時，則回傳true
print(s1.endswith('now !'))
print(s1.startswith('Learn'))

#find():尋找字串中出現S1子字串的最小索引值，並加以回傳
#rfind():尋找字串中出現S1子字串的最大索引值，並加以回傳
print(s1.find('now'))
print(s1.rfind('o'))

#strip():刪除字串兩側空白後加以回傳。
print(s1.strip())

#replace(old,new):將字串的old字元以new字元取代之
#重要:僅轉換，沒有取代
print(s1.replace('now','old'))
print(s1)                 
#split():分割後，存在串列中
s2=s1.split(' ')
print(s2)

