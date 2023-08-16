a = int(input("enter your number: "))
for i in range(1, a):
    for j in range(1, a+1):
        x = j
        while x>0:
            print(j, end=" ")
            x -= 1
        print("")
