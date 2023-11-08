#make calculater with lambda
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
oprator=str(input("enter oprator: "))
a=lambda num1,num2 : num1+num2
b=lambda num1,num2 : num1-num2
c=lambda num1,num2 : num1*num2
d=lambda num1,num2 : num1/num2
#the operation
if oprator=="+":
    print(a(num1,num2))
elif oprator=="-":
    print(b(num1,num2))
elif oprator=="*":
    print(c(num1,num2))
elif oprator=="/":
    print(d(num1,num2))