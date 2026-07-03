input1 = input("Enter a number: ")
try:
    num = int(input1)
except:
    num = -1

# Move these lines out of the except block by removing the extra spaces
if num > 0:
    print("You entered a positive number.")
else:
    print("You did not enter a positive number.")