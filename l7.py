num = int(input("enter your number: "))
total = 0
for i in range(1, num+1):
    square = i*i
    print("square of {} is: ".format(i), square)
    total += square
print("total of squares is: ", total)

