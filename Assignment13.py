#Q.1. Name and the handle the exception occured in the following program.
try:
    a=3
    if a<4:
        
     a=a/(a-3)
    print(a)
except Exception:
    print("Exception occured")
print("ZeroDivisionError")
   #ZEr
#Q.2.Name and handle the exception occured in the folowing program.

try:
    l=[1,2,3]
    print(l[3])
except Exception:
    print("exception occured")
print("index Error")
   #index error
#Q.3. what will be the output of thje following code.
#try:
   # raise NameError("Hi There") #raise error
#except NameError:
   # print("An Exception")
   # raise #to determine the exception was raised
#Answer-      raise NameError("Hi There") #raise error
              #NameError: Hi There
#Q.4. what will be the output of the following code.
# Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)

    # Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
#Answer:- -5.0
         #a/b result in 0
#Q.5.Write a program to show and handle following
    #value error
    #import error
    #index error
try:
    x=int("abc")
except Exception:
    print("Exception occured")
print("value error")
    
try:
    l=[1,2,3]
    print(l[4])
except Exception:
    print("exception occured")
print("index error")
try:
 import nice
except Exception:
    print("exception occured")
print("import error")


#Q.6.Create a user Define Exception and agetoosmallerror.
class Age(Exception):
    pass
class AgeTooSmallError(Age):
    pass
n=18
while True:
    try:
        age=int(input("enter a age"))
        if age<n :
            raise AgeTooSmallError
        elif age>n:
            print("You have entered correct age")
            break
        
    except AgeTooSmallError:
        print("you enter a wrong age which is less than 18")
    

 
