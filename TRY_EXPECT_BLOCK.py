try :
    x= int(input("Enter Number"))
    y= 10/x
    print("Result :",y)
except ZeroDivisionError :
    print("You can't divide with zero")
except ValueError:
    print("Please enter a valid")