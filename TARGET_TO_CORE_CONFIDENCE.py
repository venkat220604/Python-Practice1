#target to build core confidence
a,b =10,5
open = input("options are + - * / % // **")
match open:
    case "+" : print(a+b)
    case "-" : print(a-b)
    case "*" : print(a*b)
    case "/" : print(a/b)
    case "%" : print(a%b)
    case "//" : print(a//b)
    case "**" : print(a**b)