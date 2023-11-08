#calculater with function
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
oprator=str(input("enter oprator: "))
#function
def first(first):
    print(first + num2)
def second(second):
    print(second - num2)
def third(third):
    print(third * num2)
def fourth(fourth):
    print(fourth / num2)
#calculater
if oprator=="+":
    first(num1)
elif oprator=="-":
    second(num1)
elif oprator=="*":
    third(num1)
elif oprator=="/":
    fourth(num1)
more=str(input("do you want to add new number?y/n "))
while more=="y":
    num1=int(input("enter first number: "))
    num2=int(input("enter second number: "))
    oprator=str(input("enter oprator: "))
    if oprator=="+":
        first(num1)
    elif oprator=="-":
        second(num1)
    elif oprator=="*":
        third(num1)
    elif oprator=="/":
        fourth(num1)
    more=str(input("do you want to add new number?y/n "))
    if more=="n":
        break
