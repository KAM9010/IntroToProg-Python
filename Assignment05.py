# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Key Murray,5.16.2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #

# declare variables and constants
objFile = "ToDoList.txt"  # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""  # A menu of user options
strChoice = ""  # A Capture the user option selection

# -- Processing -- #

# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(objFile, "r")
for row in objFile:
    strData = row.split(",")
    dicRow = {"Task": strData[0].strip(), "Priority": strData[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #

# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)

    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks

    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        for dicRow in lstTable:
            print(dicRow)
        continue

    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        print("Please type a 'Task' and 'Priority'.", "\n")
        strTask = (input("Enter task:""\n")).strip()
        strPriority = (input("What is the priority of the task?(select low, medium, or high):" "\n")).strip()
        dicRow = {"Task": strTask.lower(), "Priority": strPriority.lower()}
        lstTable.append(dicRow)
        print("\n""New task has been added.")
        continue

    # Step 5 - Remove an item from the list/Table
    elif strChoice.strip() == '3':
        strTask_remove = input("Which Task would you like to remove?:""\n").strip()
        for dicRow in lstTable:
            if dicRow["Task"].lower() == strTask_remove.lower():
                lstTable.remove(dicRow)
                print("\n""Task removed!")
        continue

    # Step 6 - Save tasks to the ToDoList.txt file
    elif strChoice.strip() == '4':
        objFile = open("ToDoList.txt", "w")
        for dicRow in lstTable:
            objFile.write(dicRow["Task"] + "," + dicRow["Priority"] + "\n")
        objFile.close()
        print("\n""Tasks have been saved!")
        continue

    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("Exiting the program.")
        break
