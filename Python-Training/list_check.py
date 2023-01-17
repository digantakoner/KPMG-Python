x = [10, 20, 30, 40, 10] 
y = [75, 65, 35, 75, 30]

def check_list(li):
    if li[0] == li[-1]:
        print ("result is True")
    else:
       print ("result is False")

print("Given list : ",x)
check_list(x)
print(" y = ",y)
check_list(y)