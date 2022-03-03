#PyExceptionHandling
#PyEx3_log.py

# Import the os module
import os

# Print the current working directory
print("Current working directory: {}".format(os.getcwd()))

# Change the current working directory
os.chdir("c:/ExcelR/PythonForDS/PyExceptionHandling")

# Print the current working directory
print("Current working directory: {}".format(os.getcwd()))

try:
	fh=open("ExceptionHandling.txt","w")
	fh.write("opening the file to log error.\n")
	userinput=input("Enter any number: ")
	fh.write("User entered the number : {}\n".format(userinput))
	result = 100/int(userinput)
	fh.write("Result : {}\n".format(result))
	print("Result: ",result)
except ValueError:
	print("Not a Valid number, Enter only numbers ")
except	ZeroDivisionError:
	print("Enter Greater than 0 number ")
finally:
	fh.write("closing the file.\n")
	fh.close()
