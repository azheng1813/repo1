"""
abcdefghijklmnopqrstuvwxyz
"""
#print chr(70)
#print ord("a")
#print ord('b')
#print ord('c')
#print ord('d')
#print ord('e')
#print ord('f')
#print ord('g')
#print ord('A')
#print 65+05
List = [518, 753, 875, 1618, 1126, 615, 1613, 1966, 2062, 2412, 1173, 30, 2756, 308, 2524, 376,
918, 2528, 2169, 1359, 534, 2116, 126, 1606, 330]
Nums = []
for i in List:
	temp = str((i**3) % 2911)
	while len(temp) < 4:
		temp = "0" + temp
	first = temp[0:2]
	second = temp[2:]
	Nums.append(first)
	Nums.append(second)
for i in Nums:
	print chr(int(i) + 96),

