#print 1 tp 10 numbers

i = 1
while i<=10:
    print(i)
    i= i+1
###########

n = int(input("Enter the number : "))
i = 1
sum = 0
while i<=n :
    sum = sum + i
    i = i+1

print("Total is :" , sum)
############
n = int(input("enter the number : "))
i = 1

while i<=10:
    print(n, " * ", i , "= ", n*i)
    i= i+1
###################################

i = 1
while i <= 20 :
    if i%2==0:
        print(i, end=" ")
    else:
        print("odd", end=" ")
    i= i+1
