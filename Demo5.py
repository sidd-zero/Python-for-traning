# for i in range(1,5): #1=3
#     if i == 3:
#         break
#     print(i)

# for i in range(1,6): #1=3
#     if i == 3:
#         continue    
#     print(i)

# for i in range(5,0,-1): #1=3
#     if i == 3:
#         continue    
#     print(i)

# for i,j  in zip(range(1,6), range(5,0,-1)):
#     if i==3 and j==3:
#         continue
#     print( i, " ",j)

# i = 1
# while i<=5: 
#     print(i)
#     i = i+1


# username = ""
# password = ""
# while username != "admin" and password != "hello":
#     username = input("Enter username: ")
#     password = input("Enter password: ")

# n = int(input("Enter a number: "))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
# print("Sum is ", sum)

# name = "Prashant"
# newname= " "
# for i in name:
#     if i not in newname:
#         newname = newname + i
# print(newname)
# print(name)

# name = "Prashant"
# print(name[::-1])

# mycart= [ 10,20,200,300,800,60,700]
# for i in mycart:
#     if i > 400:
#         print("item price is more than 400, cannot proceed")
#         break
#     print(i)

# mycart= [ 10,20,200,300,800,60,700]
# for i in mycart:
#     if i > 400:
#         print("item price is more than 400, cannot proceed")
#         continue
#     print(i)

# name = "racecar"
# if name == name[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

#wap to check if two string are anagrams of each other or not , if yes print anagram
# str1 = "listen"
# str2 = "silent"
# if sorted(str1) == sorted(str2):
#     print("Anagram")
# else:
#     print("Not Anagram")

# n = int(input("Enter a number: "))
# for i in range (1, n+1):
#     for j in range(1,n+1):
#         print(n+1-i,end=" ")
#         print()
