# Student Grade Tracking System
PROJECT OVERVIEW
This is a command-line program that will help students record homework and exam results, view all assignments, filter them and see grade summaries. Everything runs in one terminal session, so data disappears once the program is closed.

# Features
- Enter homework (Subject, title, marks, max marks, due date)
- Enter exam ( subject, title, marks, max marks, exam date)
- List all assignments entered so far
- Filter assignments by subject, type, or month
- Show a grade smmary - each assignment's percentage, plus the overall average
- Checks that the marks entered connot be higher than the maximum marks

# How to Run
1. Open the project folder in VS Code
2. Open a terminal
3. Type: python main.py
4. Follow the menu on screen

# Menu Structure
1-Enter homework
2-Enter exam
3-List assignments
4-Filter by subject, type or month
5-Show grade summary
6-Close

# Sample Interaction
Choose your option from the menu list above: 1
Enter subject: Programming I
Enter title of homework: Formative I
Enter your marks: 94
Enter highest marks for the homework: 100
Enter last date for homework submission: 16/08/26
You have entered your homework assignment

# Sample Filter Interaction
Choose your option from the menu list above: 4
Enter filter type(subject/type/month): subject
Enter value to search fro: Programming I
Subject: Programming I
Title: Formative I
Marks: 94.0
Maximum Marks: 100.0
Last date: 16/08/26
Assignment category: Homework

## Classes Used
- AssignmentForm - stores one single assignment(subject, title, marks, max_marks, last_date, category)
- Homework and Exam - Inherit from Assignment Form using super(), automatically set theirown category
- AssignmentManager- manages the whole collectionof assignments: add, list, filter, and summarize08
