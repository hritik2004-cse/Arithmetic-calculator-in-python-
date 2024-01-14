print('calculator with user defined functions\n***** (+/-/×/÷)*****')

#inputting both numbers
num1= int(input('\nenter first number :'))
num2= int(input('enter second number :'))

#defining functions for operations

#addition function
def add_num(a,b):
    sum = a+b
    return sum

#subtraction function    
def subtract_num(a,b):
    sum = a-b
    return sum   

#multiplication function    
def multiply_num(a,b):
    sum = a*b
    return sum

#division function    
def divide_num(a,b):
    sum = a/b
    return sum  
 
print("\noperations available:- \n1.addition\n2.subtraction\n3.multiplication\n4.divide")  
#inputting operation by user 
choice=int(input("\nenter your operation (1/2/3/4) : ")) 

#if else statement starts here

if (choice==1):
    print("\nThe addition of {} and {} is".format(num1,num2),add_num(num1,num2))
    
elif (choice==2):
    print("\nThe subtraction of {} and {} is".format(num1,num2),subtract_num(num1,num2))    

elif (choice==3):
    print("\nThe multiplication of {} and {} is".format(num1,num2),multiply_num(num1,num2))    
    
elif (choice==4):
    print("\nThe division of {} and {} is".format(num1,num2),divide_num(num1,num2))    

else:
    print("invalid option\nplease try again")
