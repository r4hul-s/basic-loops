#A set is a collection of distinct (non-duplicate) values, 
#and is mutable (you can add or remove items).


minutes = 60


def hrs_mins(hrs):
    return f"in {hrs} hours there are {hrs*minutes} minutes"


def validate():

    try:

        entr_hours = int(list_items) #list_items = user input in form of list
        if entr_hours > 0:
            calc_mins = hrs_mins(entr_hours)
            print (calc_mins)
        elif entr_hours==0:
            print("Hours cant be zero...")
        else:
            print("You have entered negative value")    
    except ValueError:    # ValueError is a built-in exception that signals a value is wrong for the expected operation, even though the type is right.
        print("Wrong input...")

input_hrs = "" #if we dont create this empty variable the name error will appear
while input_hrs != "exit": #this will keep running the loop until we want to exit 

    input_hrs = input("Enter the hours you want to convert in minutes\n")
    print(input_hrs.split())
    print(type(input_hrs.split()))

    print(set(input_hrs.split()))
    print(type(set(input_hrs.split())))
    
    for list_items in set(input_hrs.split()): #here set function will only display the distinct values 
        validate() #calling function validate

# add any changes here 
