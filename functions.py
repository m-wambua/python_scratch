# so we will start working in fucntions

def product (num1,num2):
    prod=num1*num2
    print ('The product of the numbers is \t: '+str(prod))

num1=int(input('enter the first number\t :'))
num2=int(input('enter the second number \t:  '))
print('calling the function....')
product(num1,num2)

print('back to the calling function')