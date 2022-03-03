#PyExceptionHandling
#PyEx2.py
try:
	userinput=input("Enter any number: ")
	result = 100/int(userinput)
	print("Result: ",result)
except ValueError:
	print("Not a Valid number, Enter only numbers ")
except ZeroDivisionError:
    print("Enter Number Greater than 0")