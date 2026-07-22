# local scope variable 
def name(name):
    print(name)

name("vinay") 
# only present inside the function outside the function give error
 
 # gloable scope variable 

num = 20

def squ(num):
    print(num*num)

squ(10)
squ(num)
# can be called any where in the same code file 

# example 
city = "Delhi"

def show_city():
    country = "India"

    print(city)
    print(country)

show_city()

print(city)