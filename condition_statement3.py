# match-case

value="apple"

if value=="apple":
    print("apple is 2 dollars")
elif value=="banana":
    print("banana is 2 dollars")
elif value=="cherry":
    print("cherry is 2 dollars")

match value:
    case "apple":print("apple is 2 dollars")
    case "banana":print("banana is 2 dollars")
    case "cherry":print("cherry is 2 dollars")

score=(input("insert grade"))

match score:
    case "A": print("over 90")
    case "B": print("over 80")
    case "C": print("over 70")
    case "D": print("over 60")
    case "E": print("under 60")
    case _ : print("invalid")

