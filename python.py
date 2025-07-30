a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))

print("Here are the functions you are allowed to use :")
print("....................")
print("'*' '/' '+' '-'")
arr=input("choose in between the functions displayed i.e if you want to multiply just type * ")
if (arr=="*"):
    result=a*b
    print(result)
elif (arr=="/"):
    result=a/b
    print(result)
elif (arr=="+"):
    result=a+b
    print(result)
elif (arr=="-"):
    result=a-b
    print(result)
else:
    print("Invalid input")
