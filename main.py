#My first real python assignment
#Student Grade Tracking system
#Vincent Mussa(v.mussa@alustudent.com)-Computer Science Student(O'25)

print("Student Grade Tracking system first step.")

#Creating empty list where later will have assignments stored
#assignments like Programming I, Communication for Impact, Projects will be added in the list
assignments = []

#Crearing a class that will act like a form for assignment entry
class AssignmentForm:
    #From the the guiding instructions, assignments need to have the subject, title, score, maximum score, assignment due date and assignment type or category
    # the word _init_ is a constructor that is used to initialize each data in the class
    # Self helps to pull data from the class
    def __init__(self, subject, title, marks, max_marks, last_date, assignment_category):
        self.subject = subject
        self.title = title
        self.marks = marks
        self.max_marks = max_marks
        self.last_date = last_date
        self.assignment_category = assignment_category 

#Checking how class works with a programming assignment example
trial = AssignmentForm("Programming I", "Formative I", 94, 100, "16/08/26", "Self Work")    
print(trial.subject)  
print(f"Title: {trial.title}, Marks: {trial.marks}, Max Marks: {trial.max_marks}, Last Date: {trial.last_date}, Assignment Category: {trial.assignment_category}")                     
print(f"If you submit later than {trial.last_date}, you get zero(0) marks")

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