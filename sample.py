
pin,cash = input("please enter your pin and cash with , seperated").split(',')
cashValue = int(cash)
totalAmount= 50000  
remainingAmount=totalAmount-cashValue
print("The Amount withdrawl is : {}, The Amount remaining is : {}".format(cashValue,remainingAmount),sep=' ')
 