from pyrsistent import b


def myfunction():
    a="MyLocalObject"
    global b
    b="Global Variable"
    print("Value of Local Variable inside function ",a)
    print("Value of Global Variable inside function ",b)


myfunction()
print("Value of Global Variable Outside function ",b)