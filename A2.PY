ac=float(input("Enter the actual cost of the item:"))
sc=float(input("Enter the sell cost of the item:"))

if sc>ac:
    a=sc-ac

    print("Profit is " ,a)
elif ac>sc:
    a=sc-ac

    print("Loss is " ,a)







