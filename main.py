#My first real python assignment
#Student Grade Tracking system
#Vincent Mussa(v.mussa@alustudent.com)-Computer Science Student(O'25)

print("Student Grade Tracking system first step.")

#Crearing a class that will act like a form for assignment entry
class AssignmentForm:
    #From the the guiding instructions, assignments need to have the subject, title, score, maximum score, assignment due date and assignment type or category
    # the word __init__ is a constructor that is used to initialize each data in the class
    # Self helps to pull data from the class
    def __init__(self, subject, title, marks, max_marks, last_date, assignment_category):
        self.subject = subject
        self.title = title
        self.marks = marks
        self.max_marks = max_marks
        self.last_date = last_date
        self.assignment_category = assignment_category 

#Adding method to class
#Method is action for class to do
#First action is to show details of the assignment entered and will use indentation its part of the class
    def assignment_details(self):
        print("Subject:", self.subject)
        print("Title:", self.title)
        print("Marks:", self.marks)
        print("Maximum Marks:", self.max_marks)
        print("Last Date:", self.last_date)
        print("Assignment Category:", self.assignment_category)

#Creating class that acts as a manager for all assignment, like a physical folder at school where a teacher keeps all assignments
class AssignmentManager:
    def __init__(self):
        self.assignments = []

#Function/Method for user to add assignment to the list above
    def add_assignment(self, assignment):
        self.assignments.append(assignment)
#append is a programing word that helps add items like assignments here in the list
#after adding assignment another action is to check the assignmnents in the list/folder
    def list_assignments(self):
        if len(self.assignments) == 0:
            print("You have not entered any assignment.")
        else:
            for assignment in self.assignments:
                assignment.assignment_details()

#now the assignment manager has a list for assignments, how to add assignments, can show assignments details
#adding method to display summary for assignments
#it is used to show average marks for all subjects
    def marks_summary(self):
        if len(self.assignments) == 0:
            print("You have not entered any assignment.")
        else:
            total_percentage = 0
            for assignment in self.assignments:
                marks_percentage = (assignment.marks / assignment.max_marks) * 100
                print(f"Average for {assignment.subject}: {marks_percentage}%")
                total_percentage = total_percentage + marks_percentage
            average_percentage = total_percentage / len(self.assignments)
            print(f"The overall average percentage is {average_percentage}%")

#The lis created earlier is now a folder for the assignments and the manager
#All the menu options below will add assignments into the folder or check available assignments in the folder
assignment_manager = AssignmentManager()

#Creating function for each menu option as in the future each option can have multiple entries.
def Enter_homework():
    print("This selection allows you to enter your homework details")
#The homework has details to enter using input function from user
    subject = input("Enter subject: ")
    title_of_homework = input("Enter title of homework: ")
#float makes the text as input to numbers that can have decimals
    marks = float(input("Enter your marks: "))
    max_marks = float(input("Enter highest marks for homework: "))
    last_date = input("Enter last date for homework submission: ")
#creating assignment that enters one real homework from user
    assignment = AssignmentForm(subject, title_of_homework, marks, max_marks, last_date, "Homework")
#saving the homework to the assignment manager
    assignment_manager.add_assignment(assignment)
    print("You have entered your homework assignment.")

def Enter_exam():
    print("This selection allows you to enter your exam details")
#Just like the homework, exam has several details to be entere by user
    subject = input("Ënter subject: ")
    title_of_exam = input("Ënter title of exam: ")
    marks = float(input("Enter  your marks: "))
    max_marks = float (input("Enter highest marks for this assignment: "))
    last_date = input("Enter the exam due date: ")
#creating assignment for the manager that enters exam details from the user
    assignment = AssignmentForm(subject, title_of_exam, marks, max_marks, last_date, "Exam")
#saving exam to assignment manager
    assignment_manager.add_assignment(assignment)
    print("You have entered your exam details")

def List_assignments():
    print("This selection displays all your assignments") 
    assignment_manager.list_assignments()

def Filter():
    print("This selection allows you to filter your assignments by subject, type or month") 

def Marks_summary():
    print("This selection allows you to see your grade summary")
    assignment_manager.marks_summary()

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
        Marks_summary()

    elif user_choice == "0":
        Close()
        keep_running = False
#Here the menu list stops option if the user chooses to close

    else:
        print("Your choice is not among the list! Please try again")
#Deleted the first codes, and kept the functions for each menu option, so that in the future each option can have multiple entries.