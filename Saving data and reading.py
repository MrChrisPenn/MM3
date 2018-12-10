import csv

Quiz_Questions = []

def Load_Questions():
    print("Loading Questions....")

    csv_file = open('File.csv')

    csv_reader = csv.reader(csv_file, delimiter=',')

    #load data into class list / append



    for row in csv_reader:
        Question_Data = []
        Country,Question,Answer_A,Answer_B, Correct_Answer = row
        Question_Data.append(Country)
        Question_Data.append(Question)
        Question_Data.append(Answer_A)
        Question_Data.append(Answer_B)
        Question_Data.append(Correct_Answer)
        Quiz_Questions.append(Question_Data)

    csv_file.close()
#close excel file
    print(Quiz_Questions)#print out biscuit data

Load_Questions()

Question_Number = 0

while Question_Number < len(Quiz_Questions):
    print("Please choose one of two options.")

    print(Quiz_Questions[Question_Number][1])
    print(Quiz_Questions[Question_Number][2])
    print(Quiz_Questions[Question_Number][3])

    
    choice = input("please make your choice")
    if choice == "a" and Quiz_Questions[0][4] == "a":
        print("Correct")
    elif choice == "b" and Quiz_Questions[0][4] == "b":
        print("Correct")
    else:
        print("Incorrect")
    Question_Number = Question_Number + 1


