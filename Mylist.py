# mylist = [['prasjamt','jha'],['85.66'],[440022,"yyy"]]
# print("example of multidimesntonal list:")
# print (mylist)
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

# list1=["prashant","jha"]
# print(list1*2)

# list2=[50,25.50]
# print(list1+list2)


# list2=[50,'prashant']
# del list2[0]
# print(list2)   

# list2 = [50,25.50,'prashant']
# list2.clear()
# print(list2)

# name="prashant"
# print(name)
# myname= list(name)
# print(myname)


# mylist = [45,46,36,2324,43467,756,1,2,3,4,5,6,7,8,9]
# mylist.sort()
# print(mylist)

# #Default sorting orderr for number is ascednding
# defult sorting order for string is alphabetical order
# we should know that list should contain homogenuoys data type otherwise we will get TypeError
# python first shourt number then string follow

# math = 10
# phs =10
# eng = 20
# print(id(math))
# print(id(phs))
# print(id(eng))

# #alising means assigining one variable reference to another variable
# mylist= [ 44,22,55,6,0,9,88]
# newlist = mylist
# print(id(mylist))
# print(id(newlist))

#membership operator in list
# name= 'prashant'
# print('z' in name)
# print('z' not in name)

# for i in range(5,0,-1):
#     print(i)
    
# for i in range(1,11):
#     print(i*2," ",i*3," ",i*4, " ",i*5, " ",i*6," ",i*7," ",i*8," ",i*9," ",i*10)

# simple if
# wap to accept any digit and check that pos, neg,zero
# no = int(input("Enter any number: "))
# if no > 0:
#     print("The number is positive.")
#     if no<0:
#         print("The number is negative.")
#         if no == 0:
#             print("The number is zero.")
            
# # wap to accpt days and check the working days and weekend
# day = input("Enter the day of the week: ")
# if day in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
#     print(f"{day} is a working day.")
# elif day in ['Saturday', 'Sunday']:
#     print(f"{day} is a weekend.")
# else:
#     print("Invalid input. Please enter a valid day of the week.")


# wap to accept three paper marks and calculate total, percemtage and if percentage is greater than or equal 60 then 
# he/she is eligible for placement

# marks1 = float(input("Enter marks for paper 1: "))
# marks2 = float(input("Enter marks for paper 2: "))
# marks3 = float(input("Enter marks for paper 3: "))
# total_marks = marks1 + marks2 + marks3
# percentage = (total_marks / 300) * 100
# print(f"Total Marks: {total_marks}")
# print(f"Percentage: {percentage:.2f}%")
# if percentage >= 60:
#     print("Congratulations! You are eligible for placement.")
# else:
#     print("Sorry, you are not eligible for placement.")

#wap to accept five differen value in 5 different var and check max value and print by using "simple if statement"
value1 = float(input("Enter value 1: "))
value2 = float(input("Enter value 2: "))
value3 = float(input("Enter value 3: "))
value4 = float(input("Enter value 4: "))
value5 = float(input("Enter value 5: "))

max_value = value1 
if value2 > max_value:
    max_value = value2
if value3 > max_value:
    max_value = value3
if value4 > max_value:
    max_value = value4
if value5 > max_value:
    max_value = value5
print(f"The maximum value is: {max_value}")
