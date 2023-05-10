try:
    hours = float(input("Enter the hours : "))
    rate = float(input("Enter the Rate : "))
    if hours <= 40:
        print("enter the number")
    elif hours > 40:
        print(40 * rate + (hours - 40) * 1.5 * rate)
except:
    print("Enter the float number")


