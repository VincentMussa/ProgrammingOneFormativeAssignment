#My first real python assignment
#Student Grade Tracking system
#Vincent Mussa(v.mussa@alustudent.com)-Computer Science Student(O'25)

print("Student Grade Tracking system first step.")

#Creating empty list where later will have assignments stored
#assignments like Programming I, Communication for Impact, Projects will be added in the list
assignments = []

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

#Adding while loop to make the menu option run untill the user chooses to close when inputs 0
#The menu will show again and again until user closes program
#A note;The indentation changes because while loop will contain the if/else functions inside it
keep_running = True
#Till here the function is working but needs to be called in order to run it.
while keep_running:
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
        keep_running = False
#Here the menu list stops option if the user chooses to close

    else:
        print("Your choice is not among the list! Please try again")
#Deleted the first codes, and kept the functions for each menu option, so that in the future each option can have multiple entries.