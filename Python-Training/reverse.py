num = int(input("Enter number : "))

while(num > 0):
    reminder = num % 10
    
    num = num // 10
    print(reminder,end= " ")
