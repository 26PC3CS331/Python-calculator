#My first project
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        print("we cannot divide any number with zero")
    else:
        return a/b
print("<----Welcome to vamsi's pro Calculator---->")
print("1.Addition  (+)")
print("2.Subtration  (-)")
print("3.Multiplicaton  (*)")
print("4.Division  (/)")
print("5.All the above oprations at a time (+,-,*,/)")
choice=int(input("Select any above operation as you required  (1,2,3,4,5) : "))
if choice in (1,2,3,4,5):
    try:
        num1=int(input("Enter your first nunber : "))
        num2=int(input("Enter your second number : "))
        if choice==1:
            print(f"result :{num1}+{num2}= {add(num1,num2)}")
        elif choice ==2:
            print(f"result : {num1}-{num2}= {sub(num1,num2)}")
        elif choice ==3:
            print(f"result : {num1}*{num2}= {mul(num1,num2)}")
        elif choice==4:
            print(f"result :{num1}/{num2}= {div(num1,num2)}")
        elif choice ==5:
            print(f"Addition      : {add(num1,num2)}")
            print(f"Subtraction   : {sub(num1,num2)}")
            print(f"Mutiplication : {mul(num1,num2)}")
            print(f"Division      : {div(num1,num2)}")
    except ValueError:
        print("Error : Please enter only numbers ")
else:
    print("INVALID CHOICE")
    


