
# coding: utf-8

# In[14]:

#Get the i/p's
firstOperator = input("Please enter your first number ");
secondOperator = input("Please enter your second number ");
#Convert the i/p's 
firstOperator = float(firstOperator);
secondOperator = float(secondOperator)
# Print operations 
sum = firstOperator + secondOperator;
# Just a note the concatenation operator is ,
print("the sumition " , sum, " Herro :D!");
if sum != 0 :
    print("Sum not equal zero :D!");
    print("Sum not equal zero :D!");


# In[1]:

#Get input's 
num1 = input('enter first number ');
num2 = input('enter second number ');
#Get operation
op = input('enter the operation ');
#Converting the i/p's
num1 = float(num1);
num2 = float(num2);
#Doning the operation
if op == '+' :
    print('The summation is : ', num1 + num2 , ' :D');
elif op == '-' :
    print('The subtraction is : ', num1 - num2 , ' :D');
elif op == '*' :
    print('The multiplication is : ', num1 * num2 , ' :D');
elif op == '/' :
    print('The division is : ', num1 / num2 , ' :D');
else :
    print('Unsupported operation');


# In[1]:

list1=[0,1,2];
list1[2]=3;
print(list1);
if 1 in list1:
    print("hi");
else:
    print("bye");
list2=["salma", 1];
print(min(list1));
print(list1.index(3));
# print(list1.index(2));
list1.remove(0);
# list1.remove(0); will give an error 
tuple1 = (1, 2, "salma");



# In[9]:

str = "salma \n hy";
print(str);


# In[24]:

# loop quiz 1.Write a program which will find all such numbers 
# which are divisible by 7 but are not a multiple of 5,
found = False;
for i in range(2000, 3201):
    if i % 7 == 0 and  i % 5 != 0:
        if found: 
            print(",",end = " ");
        print(i, end="");
        found = True;


# In[40]:

# dictionary quiz
#With a given integral number n, write a program to generate a dictionary that contains
# (i, i*i) such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.
n = int(input());
dict = {}; 
for i in range(1, n+1):
    dict[i] = i*i
print (dict)


# In[42]:

# while loop
# Write a program to test a password.
# The password is secretand the code within the loop is executed until the user inputs the correct password.
PASSWORD = "salma";

userPassword = input("enter your password");
while PASSWORD != userPassword:
    userPassword = input("renter your password");
print("correct");
    


# In[44]:

# nested loops
for i in range(0,4) :
    for j in range(0,4):
        print("*", end ="");
    print();


# In[46]:

#nested loop quiz
# If we have a list of persons who like to eat at restaurants,
# print the result if every one of them will eat food from all restaurants.
persons = ["salma", "shadwa", "ahmed"];
resturants = ["MC", "KFC", "GAD", "FRA5"];
for person in persons:
    for resturant in resturants:
        print(person + " eats " + resturant);


# In[4]:

# loop flow quiz
# Write a program read a string then remove all [ spaces, * , "  , ' ] from this string then print the result.
str = input("enter yor string");
if str != "":
    for c in str:
        # if c <= '9' and c >= '0':
        if c.isdigit() == True :
            print("Data can't be processed");
            break;
    str = str.replace("*", "");
    str = str.replace(" ", "");
    str = str.replace("'", "");
    str = str.replace('"', "");
    print(str);
else:
    print("Data can't be processed"); 


# In[5]:

# python overwrite functions exactly as variable ex: x=5 x=6 x now is equal to 6 
def fn (str = "what ever"):                                                           
     print("second");
        
def fn ():                                                                        
    print("first");    
fn("salma")


# In[6]:

# call by refrence and by value
def fn (z):
    z += "sssss";
    print(z);
    
z = "aaaaaa";
fn(z);
print(z);


# In[1]:

x= 5;
def fn ():
    global x;
    z= x + 2;
    x = 6;
    print(z);
fn();
print(x);


# In[17]:

# Function quiz 1.Write a Python function to find the Max of three numbers.
def maxOfThreeNumber (num1, num2, num3):
    if (num1 >= num2 and num1 > num3):
        return num1;
    elif (num2 >= num1 and num2 > num3): 
        return num2;
    else:
        return num3;
    
# Testing.
x = int(input("enter number "));
y = int(input("enter number "));
z = int(input("enter number "));
result = maxOfThreeNumber(x, y, z);
print(result);


# In[18]:

# Function quiz 2.Write a Python function that takes a list
# and returns a new list with unique elements of the first list.
def uniqueList(list1):
    newList = [];
    for i in range(len(list1)):
        if (i+1) >= len(list1) or list1[i] != list1[i+1]:
            newList.append(list1[i]);
        
    return newList;

# Testing.
length = int(input("enter the length of list : "));
list1 = [];
for i in range(length):
    list1.append(int(input("enter an element : ")));
list2 = uniqueList(list1);
print(list2);


# In[23]:

# Function Quiz 3.Write a Python function that takes a number
# as a parameter and check the number is prime or not.


def isPrime(num):
    if (num % 2 == 0 or num == 1): return False;
    i = 3; 
    while (i*i <= num):
        if (num % i == 0): return False;
        i +=1;
    return True;

        
# Testing.
x = int(input("Enter a number : "));
if (isPrime(x)):
    print(x , "is a prime number!");
else :
     print(x , "is not a prime number!");


# In[29]:

# Function Quiz 4.Write a Python program to reverse a string.
def reversString(str):
    return str[::-1];
    
# Testing.
str1 = reversString("1234abcd");
print(str1);

