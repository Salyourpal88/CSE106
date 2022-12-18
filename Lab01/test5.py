import json
with open('grades.txt') as file:
    data = file.read()

dict = json.loads(data)
program = 'Y'

while(program != 'N'):
    print("Would you like to create student? Y/N?")
    option1 = input()
    if(option1 == 'Y'):
        print("Student Name: " , end="")
        option1 = str(input())
        print("Grade Percentage: " , end="")
        option2 = float(input())
        dict[option1] = option2

    print("Would you like to view student grade? Y/N?")
    option1 = input()
    if(option1 == 'Y'):
        print("Student Name: " , end="")
        option1 = input()
        print(dict[option1])
    
    print("Would you liket to edit a grade? Y/N?")
    option1 = input()
    if(option1 == 'Y'):
        print("Student Name: " , end="")
        option1 = input()
        print("Grade Percentage: " , end="")
        option2 = float(input())
        dict[option1] = option2
    
    print("Would you like to delete a grade? Y/N?")
    option1 = input()
    if(option1 == 'Y'):
        print("Student Name: " , end="")
        option1 = input()
        del(dict[option1])
    print("Would you like to make any other edits? Y/N?")
    program = input()
    
print("New grades.txt:")
print(dict)
file.close()