import random
x=float(50)
y=str("\"Vishwa Expert\"")
z="is"
a=str("Number one!")
def myfun():
    print(x, y, z, a,"Test is successful ra")
    print(random.randrange(1,10))
    print(y[0])
myfun()    
txt="Your friendly neighbourhood spiderman"
if "goat" in txt:
    print("The required word is present in the text!")
else:
    print("The Word is missing!")

str1='Leo,Das   '
print(str1[5:])
print(str1.split(","))    
print(str1.strip())  
print(str1.replace("Leo","Antony")) 

st2="My name is {0} and I'm {1} years old"
print(st2.format("Antony",36))
