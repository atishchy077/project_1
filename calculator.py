print('''
+ Add
- Subtract  
* Multiply
/ Divide
''')
num1=int(input("enter the value1:-"))
num2=int(input("enter the value2:-"))
opr=input("enter the operator:-")
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
    print("invalid operation")