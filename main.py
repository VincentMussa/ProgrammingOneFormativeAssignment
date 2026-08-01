#My first real python assignment
#Student Grade Tracking system
#Vincent Mussa(v.mussa@alustudent.com)-Computer Science Student(O'25)

print("Student Grade Tracking system first step.")

#Creating a function that has the menu and uses input to ask the user to make selection from the menu list
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

#Creating if/else functions to make user if selects 5, it gives Show grade summary
if user_choice == "1":
    print("This selection allows you to enter your homework assignments")

elif user_choice == "2":
    print("This selection allows you to enter your exam assignments")

elif user_choice == "3":
    print("This selection displays all your assignments") 

elif user_choice == "4":
    print("This selection allows you to filter your assignments by subject, type or month")

elif user_choice == "5":
        print("This selection allows you to see your grade summary")

elif user_choice == "0":
    print("This selection closes the program")

else:
    print("Your choice is not among the list! Please try again")

#Creating function for each menu option as in the future each option can have multiple entries.
def Enter_homework():
    print("This selection allows you to enter your homework assignments")

def Enter_exam():
    print("This selection allows you to enter your exam assignments")

def List_assignments():
    print("This selection displays all your assignments") 

def Filter():
    print("This selection allows you to filter your assignments by subject, type or month")

def Grade_summary():
        print("This selection allows you to see your grade summary")

def Close():
    print("This selection closes the program")

#Creating a function that has the menu and uses input to ask the user to make selection from the mrenu list
def menu_list():
    print(" The following is a list of menu options you are to choose from:")
    print("1-Enter homework")
    print("2-Enter exam")
    print("3-List assignments")
    print("4-Filter by subject, type or month")
    print("5-Show grade summary")
    print("0-Close")
    selection = input("Choose your option from the menu list above: ")
    return selection

#Till here the function is working but needs to be called in order to run it.
user_choice = menu_list()

#Adding if/else functions to make user if selects 5, it gives Show grade summary
if user_choice == "1":
    Enter_homework()

elif user_choice == "2":
    Enter_exam()

elif user_choice == "3":
    List_assignments()

elif user_choice == "4":
    Filter()

elif user_choice == "5":
    Grade_summary()

elif user_choice == "0":
    Close()

else:
    print("Your choice is not among the list! Please try again")

#Codes above follow the input part that printed "You have chosen the option: 1", it lacked the the if/else function
#The first codes to line 42, created one function for the menu list with the input and then created if/else functions to make user if selects 5, it gives Show grade summary
#The second codes from line 44, created function for each menu option as in the future each option can have multiple entries. Then created a function that has the menu and uses input to ask the user to make selection from the menu list. Then added if/else functions to make user if selects 5, it gives Show grade summary
#The results of the codes are the same, but the second codes are more organized, easier to read and could be used in the future if each menu option has other entries in it


