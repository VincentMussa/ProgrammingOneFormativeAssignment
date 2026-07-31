#My first real python assignment
#Student Grade Tracking system
#Vincent Mussa(v.mussa@alustudent.com)-Computer Science Student(O'25)

print("Student Grade Tracking system first step.")

#Creating a menu list in which users can choose from using print statements
print(" The following is a list of menu options you are to choose from:")
print("1-Enter homework")
print("2-Enter exam")
print("3-List assignments")
print("4-Filter by subject, type or month")
print("5-Show grade summary")
print("0-Close")

#Creating a function that has the menu and uses input to ask the user to make selection from the mrenu list
def menu_list():
    print(" The following is a list of menu options you are to choose from:")
    print("1-Enter homework")
    print("2-Enter exam")
    print("3-List assignments")
    print("4-Filter by subject, type or month")
    print("5-Show grade summary")
    print("0-Close")
    selection = input("Choose your option from the menu list above:")
    return selection
#Till here the function is working but needs to be called in order to run it.
user_choice = menu_list()
print("You have choosen the option:", user_choice)

#Creating function for each menu option as in the future each option can have multiple entries.
print(" The following is a list of menu options you are to choose from:")
def Enter_homework():
    print("This selection allows you to enter your homework assignments")

def Enter_exam():
    print("This selection allows you to enter your exam assignments")

def List_assignments():
    print("This selection allows you to list all your assignments") 

def Filter():
    print("This selection allows you to filter your assignments by subject, type or month")

def Grade_Summary():
    print("This selection allows you to show your grade summary")

def Close():
    print("This selection closes the program")




