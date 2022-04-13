shopping = ["bread", "cheese", "milk"]
shopping.append("eggs")
shopping.append("flour")
shopping.remove("cheese")
print(shopping)

while True:
    edit = input("Would you like to edit your shopping list? Y/N").upper()
    if edit == "Y":
        edit = input("Would you like to add or remove an item? A/R").upper()
        if edit == "A":
            edit = input("Enter an item to add:").lower()
            shopping.append(edit)
        elif edit == "R":
            edit = input("Enter an item to remove:").lower()
            shopping.remove(edit)
    elif edit == "N":
        break
print(shopping)
