def sub(num1, num2):
    result = num1 -num2
    return abs(result)

def add(num1, num2):
    return num1 + num2

def main():
    r = float(input("Enter a number: "))
    s = float (input("Enter another number: "))
    mySum = add(r , s)
    myDiff = sub(r , s)
    print("sum = ", mySum , "\ndif = ", myDiff)
main()