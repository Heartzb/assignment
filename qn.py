# we have the following details and  marks enter these details from the key board
student_name = input("Enter students name:\n") 
student_number = input("Enter your student number:\t") # SEP/23/BCS/14
programing = int(input("Enter  your programing marks\n")) #78
data_science = int(input("Enter your data science marks:\n")) # 89
computer_application = int(input("Enter your computer application marks: \n")) # 55
total_no_subject= int(input("Enter the total number of subject:\t"))
total_marks = programing + data_science + computer_application
print(total_marks)
average_marks = total_marks/ total_no_subject # average_marks=round((total_marks\total_no_subjects,3))
print(f"student average mark:{average_marks:.3f}\t") # print(average_marks)
# 6.write a programe that converts celius temperature to ferenheight the program should ask the user to enter the  temperature in degrees celius and display the temperature in degrees  ferenheight
#method ferenheight= (9/5c)+32
celius_temperature = float(input("Enter temperature in celius :\t"))
ferenheight = ((9/5*celius_temperature)+32)
print(f"{celius_temperature} degrees celius is equal to {ferenheight} degrees ferenheight")
# 7.A formula to calculate the cars miles per gallon
#(MPG = miles driven/gallons of gas used)
miles_driven=float(input("Enter  the miles driven "))

gallon_of_gas_used=float(input("Enter the gallons of gas used"))
MPG= miles_driven /gallon_of_gas_used
print(f"{MPG}")
 
 