print("200 is less than 300\nThis is a string") #in python we always inclosed string in single or doube quotes 
print(3)#this is an integer datatype
print(4.5)#this is an float datatype
#string concatination= when we combine string with any calculation or any number 
print(20*24*60)
print("There are "+ str(28800) + " minutes in 20 days")
    #or
print(f"There are {28800} minutes in 20 days")  
   #or
print(f"There are {20*24*60} minutes in 20 days")  #more convienent for string concatinaton

#python is dynamically typed = {x=3 it automatically identifies it as an integer}

'''False      await      else       import     pass
   None       break      except     in         raise
   True       class      finally    is         return
   and        continue   for        lambda     try
   as         def        from       nonlocal   while
   assert     del        global     not        with
   async      elif       if         or         yield''' #these are reserved keywords in python

#variable example

calculation_to_seconds = 20*24*60*60 #calculation_to_sec is a variavle name
print(f"There are {calculation_to_seconds} seconds in 20 days")

#functions are used to avoid the repetition of the same logic 

calculation_to_seconds = 20*24*60*60


def days_to_units(): #function define
    print(f"There are {calculation_to_seconds} seconds in 20 days")
    print("All awesome!")


days_to_units() # calling function{this will print the above two print statements}

calculation_to_units = 24
name_unit = "hours"



def days_to_units(num_days): #function define
    print(f"{num_days} days are {num_days * calculation_to_units} {name_unit}")
    print("All awesome!")


days_to_units(10) #this will print the number of hours in 10 days
days_to_units(20) #this will print the number of hours in 20 days
days_to_units(30) #this will print the number of hours in 30 days
days_to_units(40) #this will print the number of hours in 40 days