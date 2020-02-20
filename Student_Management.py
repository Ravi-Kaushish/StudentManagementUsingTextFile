FILEPATH='C:\\Users\\ravikant.sharma\\Desktop\\PracticeAppFile'
FILENAME='PAF'
DEFAULTFILEFORMAT='.txt'
FULLFILENAME=FILEPATH + '\\' + FILENAME + DEFAULTFILEFORMAT

#This function will help the user to get started with the process
def OperationInitialzer():
    print("""Welcome to Student Details Management System
            1. Press 1 to View All Student Details .
            2. Press 2 to Add a New Student .
            3. Press 3 to Update Student Details .
            4. Press 4 to Delete Student Details .
            5. Press 5 to Search Student by Name .
    """)
    userChoice = int(input("Please Enter a Number to perform Operation mentioned against it : \t"))
    print("\n")
    UserChoiceHandler(userChoice)
    print("\n")
    return input("Type 'Yes' to perform another Operation or press any 'key' to exit : \t")
 
#File Write Handler
def FileWriteHandler(textToWrite):
    try:	
        FileToHandle = open(FULLFILENAME,'a+')
        FileToHandle.writelines(textToWrite) 
        FileToHandle.close()
        print("Student details are Added successfully")
    except:
        print("An unexpected error has occured, Please try Again!")

#This Function Handles the String Manipulation to write to the file
def StudentDetailStringHandler(studentid, firstname, lastName, city, state):
    studentInfoToAdd = []
    studentInfoToAdd.append(studentid)
    studentInfoToAdd.append('.')
    studentInfoToAdd.append(firstname)
    studentInfoToAdd.append('.')
    studentInfoToAdd.append(lastName)
    studentInfoToAdd.append('.')
    studentInfoToAdd.append(city)
    studentInfoToAdd.append('.')
    studentInfoToAdd.append(state)
    studentInfoToAdd.append('.')
    studentInfoToAdd.append('\n')
    FileWriteHandler(studentInfoToAdd)

#View Student Details Request Handler
def ViewAllStudents():
    with open(FULLFILENAME, "r+") as FileToRead:
        AllStudentDetails = FileToRead.readlines()
        print("%-10s %-20s %-20s %-15s %-12s" % ("Student ID","First Name","Last Name","City","State"))        
        for studentDetail in AllStudentDetails:
            currentStudentdetails = list(studentDetail.split('.', 5))
            print("%-10s %-20s %-20s %-15s %-12s" % (currentStudentdetails[0],currentStudentdetails[1],currentStudentdetails[2],currentStudentdetails[3],currentStudentdetails[4]))
    FileToRead.close()

#Add Student Details Command Handler
def AddNewStudent():
    studentId   = input("Enter Student's ID : \t")
    firstName   = input("Enter Student's First Name : \t")
    lastName    = input("Enter Student's Last Name : \t")
    city        = input("Enter Student's City : \t")
    state       = input("Enter Student's State : \t")
    print("\n")
    StudentDetailStringHandler(studentId,firstName,lastName,city,state)

#Update Student Details Command Handler
def UpdateStudentDetails():
    studentIDToUpdate= input("Enter the Student ID to Update the Student Details : \t")
    newfirstName   = input("Enter Student's  New FirstName : \t")
    newlastName    = input("Enter Student's New LastName : \t")
    newcity        = input("Enter Student's New City : \t")
    newstate       = input("Enter Student's New State : \t")
    with open(FULLFILENAME, "r+") as FileToRead:
        AllStudentDetails = FileToRead.readlines()
    FileToRead.close()
    with open(FULLFILENAME, "w+") as FileToHandle:
        count = 0
        for studentDetail in AllStudentDetails:
            currentStudentdetails = list(studentDetail.split('.', 5))
            if studentIDToUpdate != currentStudentdetails[0]:
                FileToHandle.write(studentDetail)
            else:
                count +=1
                if len(newfirstName)==0:
                    newfirstName=currentStudentdetails[1]
                if len(newlastName)==0:
                    newlastName =currentStudentdetails[2]
                if len(newcity)==0:
                    newcity     =currentStudentdetails[3]
                if len(newstate)==0:
                    newstate    =currentStudentdetails[4]
                studentInfoToUpdate= studentIDToUpdate  + '.' + newfirstName + '.' + newlastName + '.' + newcity + '.' + newstate + '.' + '\n'
                FileToHandle.write(studentInfoToUpdate)
                print("Student details are Updated successfully\n")
                print("Updated Details are : \t")
                print("%-10s %-20s %-20s %-15s %-12s" % ("Student ID","First Name","Last Name","City","State"))
    FileToHandle.close()
    if count == 0:
        print("Error! Such Student doesn't exist")
        allowNewEntry=int(input("Do you want to make a new entry with these Details? press 1 if yes, or press any key to abort : \t"))
        if allowNewEntry == 1:
            FileToHandle.close()
            StudentDetailStringHandler(studentIDToUpdate, newfirstName, newlastName, newcity, newstate)
        else:
            print("Dropping the above Entered Details")

#Delete Student Details Command Handler
def DeleteStudentDetails():
    studentIDToDelete= input("Enter the Student ID to delete the Student Details : \t")
    with open(FULLFILENAME, "r+") as FileToRead:
        AllStudentDetails = FileToRead.readlines()
        FileToRead.close()
    with open(FULLFILENAME, "w+") as FileToHandle:
        count = 0
        for studentDetail in AllStudentDetails:
            currentStudentdetails = list(studentDetail.split('.', 5))
            if (studentIDToDelete != currentStudentdetails[0]):
                FileToHandle.write(studentDetail)
            else:
                count += 1
        if count > 0:
            print("Deleted the Student Details successfully")
        else:
            print("Error! Such Student doesn't exist")
    FileToHandle.close()
        
#Search Student By Name Request Handler
def SearchByStudentName():
    studentNameToSearch= input("Enter the full or Partial Student Name to search through the File : \t")
    print("\n")
    with open(FULLFILENAME, "r+") as FileToRead:
        count = 0
        AllStudentDetails = FileToRead.readlines()
        print("%-10s %-20s %-20s %-15s %-12s" % ("Student ID","First Name","Last Name","City","State"))          
        for studentDetail in AllStudentDetails:
            currentStudentdetails = list(studentDetail.split('.', 5))
            if (studentNameToSearch in currentStudentdetails[1].lower()):
                print("%-10s %-20s %-20s %-15s %-12s" % (currentStudentdetails[0],currentStudentdetails[1],currentStudentdetails[2],currentStudentdetails[3],currentStudentdetails[4]))
                count += 1
        if count == 0:
            print("Entered Name (SubString) Doesn't match any student Name")
        print("\n")
    FileToRead.close()

#userChoice Operation Handler
def UserChoiceHandler(userChoice): 
    if (userChoice==1):
        ViewAllStudents()
    elif (userChoice==2):
        AddNewStudent()
    elif (userChoice==3):
        UpdateStudentDetails()
    elif (userChoice==4):
        DeleteStudentDetails()
    elif (userChoice==5):
        SearchByStudentName()
    else:
        print("Please Enter a valid Operation : \t")
        print("\n")
        OperationInitialzer()

#Handling the number of times program runs 
run='yes'
while run.lower()=='yes':
    re_run=OperationInitialzer()
    print("\n")
    if re_run.lower()=='yes':
        run==re_run.lower()
    else:
        run="exit"
        print("Quiting the program, Thank you!")
        break