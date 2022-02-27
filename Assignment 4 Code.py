print("Question 1")
#Defining the tower of Hanoi:
def tower_of_hanoi(n , Source, Destination, Auxiliary):
    step_n=1
    if n==1:
        print ("Move disk 1 from",Source,"to",Destination)
        return
    tower_of_hanoi(n-1, Source, Auxiliary, Destination)
    print ("Move disk",n,"from",Source,"to",Destination)
    tower_of_hanoi(n-1, Auxiliary, Destination, Source)
#taking number of disk input from the user
numb=int(input("Enter the Number of Disks in Tower of Hanoi="))
print("\nThe Disks are numbered starting from top of the tower."
      "\nSteps to move all disks from Source Tower to Destination Tower "
      "is given below:\n")
#Using the function of tower of hanoi
tower_of_hanoi(numb,"Source Tower","Destination","Auxiliary")
print("***********************************************************************")
print(" ")


print("Question 2")
# input n
n = int(input("Enter upto which number you have to print Pascal's Triangle="))
#Using Recursion Method
print("The Pascal Triangle using recursion method is : ")
def pascal_triangle(numb):
    if numb ==1:
        return [[1]]  #returning '1' if user enter only 1 as in pascal triangle
    else :
        result = pascal_triangle(numb - 1)  
        current_row = [1]
        previous_row = result[-1]
        for i in range(len(previous_row)-1) :
            current_row.append(previous_row[i] + previous_row[i+1])
        current_row += [1]
        result.append(current_row)  
    return result  # Recursive result 
for i in pascal_triangle(n):
    print((n - len(i))*" ",end="")
    for j in  i:
        print(j,end=" ")
    print()
    

#Using Iteration Method   
print("The Pascal Triangle using iteration method is : ")
# I am using Binomial Coefficients to print Pascal's triangle

for i in range(1, n+1):
    for j in range(0, n-i+1):
        print(' ', end='')
 
    # first element is always 1
    x = 1
    for j in range(1, i+1):
 
        # first value in a line is always 1
        print(' ', x, sep='', end='')
 
        # using Binomial Coefficient
        x = x * (i - j) // j
    
    print()
print("***********************************************************************")
print(" ")


print("Question 3")
#Taking input from the user
n1=int(input("\nEnter an integer="))
n2=int(input("Enter another integer="))
#Defining a function for quotient and remainder
def q_and_r_finder(x,y):
    quotient = (x // y)
    remainder = (x % y)
    return quotient,remainder
#Making a list of return values
list_=list(q_and_r_finder(n1,n2))
#a1=Quotient
q=list_[0]
#a2=Remainder
r=list_[1]
#printing the quotient and remainder
print(f"\nThe quotient when {n1} is divided by {n2} is {q}.")
print(f"The remainder when {n1} is divided by {n2} is {r}.")
#Que3.a
print("\nQue3(a)")
i=callable(q_and_r_finder)  #printing if function is callable or not
j=callable(n1)
k=callable(n2)
if i==True:
    print(f"Function is callable")
if i==False:
    print(f"Function is Not-callable")
if j==True:
    print(f"{n1} is callable")
if j==False:
    print(f"{n1} is Not-callable")
if k==True:
    print(f"{n2} is callable")
if k==False:
    print(f"{n2} is Not-callable")
#Que3.b
print("\nQue3(b)")
#list of values
list0=[q,r]
zero=False
if zero in list0:
    zero=True
else:
    zero=False
if zero==True:
    print("All result values are NOT 'non-zero'")
elif zero==False:
    print("All result values are 'non-zero'")
#Que3.c
print("\nQue3(c)")
#new values of list
list1=[q,r]
for i in range (4,7):
    list1.append(i)
list2=[]
#adding number > 4 from list1 to list2
for i in list1:
    if i>4:
        list2.append(i)
#defining a new list, list3 with same elements as list2 but in string form
list3=list(map(str,list2))
#Using join
v=",".join(list3)
print(f"Values greater than 4 is {v}")
#Que3.d
print("\nQue3(d)")
set1={1,2}
set1.clear()
#adding above result in set datatype
for el in list2:
    set1.add(el)
print("Above result in set form is shown below:")
print(set1)
#Que3.e
print("\nQue3(e)")
#Making set1 immutable
frozenset(set1)
print("The above set has been converted to immutable.")
#Que3.f
print("\nQue3(f)")
print(f"Max value from set is {max(set1)}")
#using hash function
hash_value=hash(max(set1))
print(f"Hash value of {max(set1)} is {hash_value}")
print("***********************************************************************")
print(" ")



print("Question 4")
#forming a class named student
class student:
    #using constructor to create class objects
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    #defining print function
    def pfun(self):
        print(f"Hello, My Name is {self.name} and My"
              f"Roll No. is {self.roll_no}")
    #calling destructor
    def __del__(self):
        print("Destructor Called")
#making 'abc' an object of student
abc=student("Keshav Singh",21104125)
abc.pfun()
del abc
print("***********************************************************************")
print(" ")



print("Question 5")
#forming class employees
class employees:
    #Using constructor to for class objects
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def pfun(self):
        print(f"Employee Name is {self.name} and Salary is {self.salary} ")
#emp_n name and salaray
emp_1=employees("Mehak",40000)
emp_2=employees("Ashok",50000)
emp_3=employees("Viren",60000)
#print employee detail
emp_1.pfun()
emp_2.pfun()
emp_3.pfun()
#Updating salary of Mehak to 70000
print("\nQue(5a)")
emp_1.salary=70000
print("Mehak salary Updated to 70000")
emp_1.pfun()
#Deleting Viren's data
print("\nQue(5b)")
del emp_3
print("Employee Viren's data has been removed.")
print("***********************************************************************")
print(" ")




print("Question 6")
gap=" "*10
print(f"\n{gap}WELCOME TO THE GAME")
#definig principle of game
print(" ")
def game(word1,word2):
    #converting all letters to lowercase
    word1=word1.lower()
    word2=word2.lower()
    #form empty list to store letters of words
    l0=[]
    l1=[]
    for e in word1:
        l0.append(e)
    for el in word2:
        l1.append(el)
    #sorting the list alphabetically
    l0.sort()
    l1.sort()
    if l0==l1:
        return True
    else:
        return  False
               
#taking player name input
player1=str(input("Enter Player1 name:"))
player2=str(input("Enter Player2 name:"))
#taking words spoken by written
word_player1=str(input(f"\nEnter Word by {player1}:"))
word_player2=str(input(f"Enter Word by {player2}:"))
#calling the game function
result=game(word_player1,word_player2)
#printing the final result
if result==True:
    print(f"\nFriendship of {player1} and {player2} is REAL.")
elif result==False:
    print(f"\nFriendship of {player1} and {player2} is FAKE.")
print("***********************************[THE--END]***********************************")    
