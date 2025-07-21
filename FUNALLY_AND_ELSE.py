try :
    num = int(input("Enter the number :"))
except ValueError :
    print("Invalid")
finally:
    print("This block always  runs")