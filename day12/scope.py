#their is nothing the term "block scoping" in python
#local scope - variable declared inside the function are treated as local scope 
# def local_scope():
#     local="name"
#     print(f"variable inside the function: {local}") #this will pring name
# local_scope()
# print(f"variable inside the function: {local}") #this will give error as no variable has with the name local outside the function


#global scoping - accessible both inside and outside of the function
# variable=12

# def my_function():
#     print("glabal variable inside the function: ", variable)

# my_function()

# print(f"glabal variable outside the function: {variable}")

# if we have to change the global variable inside th function then we have to use "global" keyword to refere global variable
def modify_global_variable():
    global variable
    variable = 15
    print(f"variable after modifying inside the function: {variable} ")

modify_global_variable()
print(f"variable after modifying inside outside the function: {variable} ")
