name     = input("enter your name= ") # input for the name of the user
rollno   = int(input("enter you rollno.=")) 

# these are the user input for the subject which we want in MarkSheet
eng      = int(input("enter your English no= "))
hindi    = int(input("enter your Hindi no= "))
math     = int(input("enter your Math no= ")) 
computer = int(input("enter your Computer no= "))
social   = int(input("enter your Social no= "))
science  = int(input("enter your  Science no= "))

total = eng+hindi+math+computer+social+science #formula to find total marks of all subject
percentage = (total/600)*100 # formula to find percentage 

print("\n")
print("\t class 10 marksheet")
print("-"*50+"|") #("-") The line is called hyphens & used to create a visual separator in the output.
print("Name of student: ",name)
print("student Rollno.: ",rollno)
print("="*50+"|")

print("subject","\t","mark obtained","\t","grade")
print("-"*50+"|")

# nested if else statement to find the grade 
if eng >= 90:
    print("English","\t"*2,eng,"\t","A+")  # \t  is called a tab character. It is used to insert a horizontal tab space in a string.
elif eng >= 80:
    print("English","\t"*2,eng,"\t","A")    #it may take 4 space in one tab.
elif eng >= 70:
    print("English","\t"*2,eng,"\t","B+")   # elif statement we used because we have multiple condition.
elif eng >= 60:
    print("English","\t"*2,eng,"\t","B")
elif eng >= 50:
    print("English","\t"*2,eng,"\t","C+")
elif eng >=40:
    print("English","\t"*2,eng,"\t","C")
elif eng >=34:
    print("English","\t"*2,eng,"\t","D+")
else:
    print("English","\t"*2,eng,"\t","FAIL")
    
# nested if else statement to find the grade 
if math >= 90:
    print("math","\t"*3,math,"\t","A+")
elif math >= 80:
    print("math","\t"*3,math,"\t","A")
elif math >= 70:
    print("math","\t"*3,math,"\t","B+")
elif math >= 60:
    print("math","\t"*3,math,"\t","B")
elif math >= 50:
    print("math","\t"*3,math,"\t","C+")
elif math >=40:
    print("math","\t"*3,math,"\t","C")
elif math >=34:
    print("math","\t"*3,math,"\t","D+")
else:
    print("math","\t"*3,math,"\t","FAIL")
    
# nested if else statement to find the grade 
if hindi >= 90:
    print("hindi","\t"*3,hindi,"\t","A+")
elif hindi >= 80:
    print("hindi","\t"*3,hindi,"\t","A")
elif hindi >= 70:
    print("hindi","\t"*3,hindi,"\t","B+")
elif hindi >= 60:
    print("hindi","\t"*3,hindi,"\t","B")
elif hindi >= 50:
    print("hindi","\t"*3,hindi,"\t","C+")
elif hindi >=40:
    print("hindi","\t"*3,hindi,"\t","C")
elif hindi >=34:
    print("hindi","\t"*3,hindi,"\t","D+")
else:
    print("hindi","\t"*3,hindi,"\t","FAIL")
    
 # nested if else statement to find the grade    
if computer >= 90:
    print("computer","\t"*2,computer,"\t","A+")
elif computer >= 80:
    print("computer","\t"*2,computer,"\t","A")
elif computer >= 70:
    print("computer","\t"*2,computer,"\t","B+")
elif computer >= 60:
    print("computer","\t"*2,computer,"\t","B")
elif computer >= 50:
    print("computer","\t"*2,computer,"\t","C+")
elif computer >=40:
    print("computer","\t"*2,computer,"\t","C")
elif computer >=34:
    print("computer","\t"*2,computer,"\t","D+")
else:
    print("computer","\t"*2,computer,"\t","FAIL")
    
  # nested if else statement to find the grade   
if social >= 90:
    print("social","\t"*3,social,"\t","A+")
elif social >= 80:
    print("social","\t"*3,social,"\t","A")
elif social >= 70:
    print("social","\t"*3,social,"\t","B+")
elif social >= 60:
    print("social","\t"*3,social,"\t","B")
elif social >= 50:
    print("social","\t"*3,social,"\t","C+")
elif social >=40:
    print("social","\t"*3,social,"\t","C")
elif social >=34:
    print("social","\t"*3,social,"\t","D+")
else:
    print("social","\t"*3,social,"\t","FAIL")
    
  # nested if else statement to find the grade   
if science >= 90:
    print("science","\t"*2,science,"\t","A+")
elif science >= 80:
    print("science","\t"*2,science,"\t","A")
elif science >= 70:
    print("science","\t"*2,science,"\t","B+")
elif science >= 60:
    print("science","\t"*2,science,"\t","B")
elif science >= 50:
    print("science","\t"*2,science,"\t","C+")
elif science >=40:
    print("science","\t"*2,science,"\t","C")
elif science >=34:
    print("science","\t"*2,science,"\t","D+")
else:
    print("science","\t"*2,science,"\t","FAIL")



print("-"*50+"|")

if eng >= 34 and math >= 34 and hindi >= 34 and computer >= 34 and social >= 34 and science >= 34:
    print("Total mark:","\t"*2,total)               # f-strings make it easy to insert values or expressions directly into a string.
    print(f"{"Percentage:"}\t\t{ percentage:.2f}%") # .2f ensures that the percentage is always displayed with exactly two decimal places.providing a clean and standardized output.
    if percentage >= 90:
        print("Grade","\t"*3,"A+")
    elif percentage >= 80:
        print("Grade","\t"*3,"A")
    elif percentage >= 70:
        print("Grade","\t"*3,"B+")
    elif percentage >= 60:
        print("Grade","\t"*3,"B")
    elif percentage >= 50:
        print("Grade","\t"*3,"C+")
    elif percentage >= 40:
        print("Grade","\t"*3,"C")
    elif percentage >= 34:
        print("Grade","\t"*3,"D+")
    else:
        print("Grade","\t"*3,"FAIL")
    
    if percentage >=34:
        print("congratulation ! ! ! you score well","\U0001F600")
    else:
        print("work hard for better result","\U0001F622")
        
else:
    print("Total mark:","\t"*2,"Error")
    print("Percentage:","\t"*2,"Error")
    print("Grade     :","\t"*2,"Error")
    print("\n","Better luck next time!!!!!!")
    
    
    
    
    
    

