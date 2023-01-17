num = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	ele = int(input())
	num.append(ele)
print(num)
print("divisable by 5:")
for i in range(0, n):
    if (num[i]%5==0):
        print (num[i])
