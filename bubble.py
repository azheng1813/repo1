A = [11,4,16,12,5]
n = len(A) 
swapped = True
while swapped:
	swapped = False
	for i in range(1,n):
		if A[i-1] > A[i]:
			temp = A[i-1]
			A[i-1] = A[i]
			A[i] = temp
			swapped = True
print A