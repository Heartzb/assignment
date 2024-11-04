#The volume of a sphere with radius r is (4/3)*pie*r**2.
# What is the volume of
# The volume of asphere with radius r is (4/3)*pie*r**2 .
#What is the volume of a sphere with radius 5
# make sure the programeenters the radius from the keyboard and provide the the answers 2 decimal places
#answers
radius = int(input('Enter the radius of the sphere:\t'))
pie = float(input('Enter the pie of the sphere: \t'))
volume = (4/3)*pie*radius**2
print(f'The volume of the sphere of {radius} and {pie} is {volume:.2f}')


# qn 2
#Creata a progrome to calculate the area of a triangle (1/2* base*height)
# base and height should be entered using keyboard
 
                         # answer
base = int(input('Enter base of the triangle:\t')) 
height = int(input('Enter height of the triangle: \t'))
area = (1/2)*base*height
print(f'The area of a triangle of {base} and {height} is {area}')                      
 
 #qn3
 # Witi has tasked you to automate a simple grading system .
 # As a python student, write a progrome using to display the grades that
 #the student will be receiving based on the mark scored in the subject
 # The grades are: 
 # 90%-100% Grade is A
 # 80%-89% Grade is B
 #70%-79%  Grade is C
 # 60%-69% Grade is D
 #50%-59% Grade IS E
 #< 50% Fail
 
                           # answers
mark = int(input('Enter the mark scored : \t'))
if mark>=90 and mark<=100:
        print('Grade is A')
elif mark>=80 and mark<=89:
        print('Grade is B')
elif mark>=70 and mark<=79:
        print('Grade is C')
elif mark>=60 and mark<=69:
       print('Grade is D')
elif mark>=50 and mark<=59:
        print('Grade is E')

else:
      print('Fail')

      

 
#qn4
# Witi Academy is proposing a sacco to help students save their money.
# Design a platform that will do the following .
# Welcome to ,Witi academy sacco.
# 1.Deposit money
# 2.withdraw money
# 3.check balance
# Ensure if the students selects 1,money is deposited and the minimum deposit should be 1000
# If the students selects 2, money should be withdrawn and the minimum withdrawal is 500
# If the students selects 3, the account balance should be displayed

# answers 4
print("Welcome to, WITI Academy sacco")
account_balance = 0
run = 1
while run ==1:
      print("1.Deposit money")
      print('2.Withdraw money')
      print('3.Check balance')
      selection=int(input("Enter desired option 1,2 or 3"))
student_option = int(input('Enter your selection(1,2,or 3')) 
if student_option==1:
    print('n\...processing a deposit transaction...')
    deposit_amount = int(input('Enter amount to be deposited')) 
if deposit_amount<1000:
       print("The minimum deposit should be 1000")
elif student_option==2:
   withdraw_amount= int(input("Enter withdraw Amount"))
if withdraw_amount<500:
       print(" The minimum withdraw is 500")
       

    
elif student_option==3:
       
    account_balance = deposit_amount- withdraw_amount
    print(f"The account balance is{account_balance}")
else:
    print('You entered a wrong option!!please select 1,2,or3\n')
    

     

