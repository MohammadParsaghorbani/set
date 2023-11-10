import turtle as t

work_list=["hi","hello","open bakery","bakery","calculater","open calculater","draw shape"]
draw_shape=["triangle","Square"]

hello=input(": ")
if hello in (work_list[1]) or hello in (work_list[0]):
    work=input("Hi,who can i help you: ")
    if work in (work_list[2]) or work in (work_list[3]):
        total_1=0
        total_2=0
        total_3=0
        total_4=0
        total_5=0
        total_6=0
        total_7=0

        bakery={
            "sangak":4000,
            "barbary":1500,
            "lavash":2000,
            "taftoon":3550,
            "baget":5000,
            "nylon":500
        }
        a=0
        print("=========================================================")
        print("Welcom to psrsa bakery!")
        name=input("please enter your name: ")
        password_1=input("please enter yor password: ")
        password_2=input("enter your password again:")
        checout="nothing"

        ########################======================***************===========================###############################

        for password in range(2):
            while password_1 != password_2:
                print("wrong password!")
                password_2=input("try again: ")
        print("yor password is accepted")
        while checout != "done":
            if a==0:
                checout=input(f"dear {name} plz enter your bread: ")
            else:
                checout=input("plz enter your next item: ")
            while checout not in dict(bakery):
                if checout=="done":
                    break
                checout=input("plz enter existing bread: ")
            if checout=="done":
                break
            customer=int(input(f"how many {checout} do you want: "))
            if checout=="sangak":
                total_1=bakery["sangak"]*customer+total_1
                print(f"your total={total_1}T")
            elif checout=="barbary":
                total_2=bakery["barbary"]*customer+total_2
                print(f"your total={total_2}T")
            elif checout=="lavash":
                total_3=bakery["lavash"]*customer+total_3
                print(f"your total={total_3}T")
            elif checout=="barbary":
                total_4=bakery["taftoon"]*customer+total_4
                print(f"your total={total_4}T")
            elif checout=="barbary":
                total_5=bakery["baget"]*customer+total_5
                print(f"your total={total_5}T")
            elif checout=="nylon":
                total_6=bakery["nylon"]*customer+total_6
                print(f"your total={total_6}T")
            a=1
        place=int(input("how far are you?/meters: "))
        if place<=0 and place<=200:
            print("you have free delivery!")
            total_7=total_7+0
        elif place>=201 and place<=500:
            print("you must pay 20000T")
            total_7=total_7+20000
        elif place>=501 and place<=1000:
            print("you must pay 45000T")
            total_7=total_7+45000
        else:
            total_7=total_7+62500
        total=total_1+total_2+total_3+total_4+total_5+total_6+total_7
        print(f"your cost = {total}T")
    elif work in (work_list[4]) or work in (work_list[5]):
        calculater_list=["calculater","open calculater"]
        num1=int(input("enter first number: "))
        num2=int(input("enter second number: "))
        oprator=str(input("enter your oprator: "))
        lambda1=lambda num1,num2:num1+num2
        lambda2=lambda num1,num2:num1-num2
        lambda3=lambda num1,num2:num1*num2
        lambda4=lambda num1,num2:num1/num2
        lambda5=lambda num1,num2:num1**num2
        lambda6=lambda num1,num2:num1%num2
        if oprator=="+":
            print(lambda1(num1,num2))
        elif oprator=="-":
            print(lambda2(num1,num2))
        elif oprator=="*":
            print(lambda3(num1,num2))
        elif oprator=="/":
            print(lambda4(num1,num2))
        elif oprator=="**":
            print(lambda5(num1,num2))
        elif oprator=="%":
            print(lambda6(num1,num2))
##########################################################################
    elif work in (work_list[6]):
        shape=input("which one: triangle or Square? ")
        if shape in (draw_shape[0]):
            for i in range(3):
                t.fd(200)
                t.right(120)
        elif shape in (draw_shape[1]):
            for i in range(4):
                t.fd(150)
                t.right(90)