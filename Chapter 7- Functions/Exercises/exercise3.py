def make_shirt(size,message):
    print("The size and the message for the given shirt is:",size,message)

#Call the make_shirt function with specific size and message arguments.
make_shirt(3,"BSU")

#OR

#Alternatively, interactively  get the shirt size and message from the user using input().
#Store the values entered by the user in the size and msg variables.
size=int(input("Enter your shirt size:"))
size=int(input("Enter your shirt size:"))
msg=input("Enter the message!:")

#Call the make_shirt function with the values entered by the user.
make_shirt(size,msg)