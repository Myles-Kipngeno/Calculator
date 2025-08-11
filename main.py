from calculator import *

while True:  
    print("1 - Addition")
    print("2 - Subtract")
    print("3 - Multiply ")
    print("4 - Divide")
    print("5 -Remainder")
    print("6 - Exit")
    option = eval(input("Choose an operation: "))

   
    

    if option == 6:
         print("Exiting the program...Good bye!")        
         break
    else:
           
         num1 = eval(input("Enter the first number: "))
         num2 = eval(input("Enter the second number:"))
                  

         if( option == 1):
            result = add(num1 , num2)
         elif(option == 2):
               result = sub(num2, num1)
         elif(option == 3):
               result = multiply(num1 ,num2)
         elif(option == 4):   
               result = divide(num1 ,num2) 
         elif(option == 5):
                result = remainder(num2, num1)
         else:
                print("Invalid operation entered.")
  
    print(f"The result of the operation is {result}")

  