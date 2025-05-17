# list & for loop, list used to store multiple items in a single variable, represented by '[]'
# for loop similar to  while loop but the number of iterations is known in for loop 


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
    for list_items in input_hrs.split(): #split is a funtion which takes user input and convert it into list
        validate() #calling function validate