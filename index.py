# print("Welcome to python 101")
# print("Welcome to python 101")
# print("Create hammer")
# print("Use hammer")


# failed_subjects="2"
# name="Eric"
# # Boolean True or False
# a="it's"
# b='it\'s'
# print('Dear Mrs Badger')
# print('Your son '+ name +' is failing ' + failed_subjects + ' subjects.')
# print(name + ' will need to redo ' + failed_subjects + 'courses.')
# name="John"
# print(name + ' is doing well in geography.')


# print(type('hello'))
# print(type(1))
# print(type(1.64))
# print(type(True))




# # Changing Integers to Strings print('The number of students in the classroom is ' + str(30))
# classroom = 30
# print('The number of students in the classroom is ' + str(classroom))


# a = int(1)        # a will be 1
# b = int(2.5)      # b will be 2
# c = int("3")      # c will be 3
# c1 = int(float("3.4"))   # c1 will be...
# d = float(1)      # d will be 1.0
# e = float(2.5)    # e will be 2.5
# f = float("3")    # f will be 3.0
# g = float("4.23") # g will be 4.23
# h = str("80s")    # h will be '80s'
# i = str(22)       # i will be '22'
# j = str(3.01)     # j will be '3.01'

# print([a,b,c,d,e,f,g,h,i,j])


# item_name = "hammer"
# item_price = 10.99
# item_quantity = 5
# is_in_stock = True
# print (item_name, item_price, item_quantity)

# name = input (" What is your name?:")
# age = input ("What is your age?: ")
# print("Hello " + name + "! You are " + age + " years old." )

# Build a calculator that can add, subtract, multiply, and divide two numbers.

# num1 = input("Enter a digit: ")
# num2 = input("Enter a second number: ")
# answer= float(num1) + float(num2)
# print(answer)

# Distance Converter
# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

# name = input ("What is your name?:")
# distance = input ("What is the distance in km?: ")
# miles = float(distance)/ 1.609
# print ("Hello " + name + "the distance is " + str(float(miles)) + "m in miles" )
# Using f string and string literals
# print(f'Hi {name.title()}! {distance}km is equivalent to {miles}')


# a=6
# b=2
# print('Addition : ', a + b)
# print('Subtraction : ', a - b)
# print('Multiplication : ', a * b)
# print('Division (float) : ', a / b)
# print('Division (floor) : ', a // b)
# print('Modulus : ', a % b)
# print('Exponent : ', a ** b)

# msg='welcome to Python 101: Strings'
# print(msg)
# print(msg.upper())
# print(msg.lower())
# print(msg.capitalize())


# Strings
# msg='welcome to Python 101: Strings'
# print(msg+msg) # Concatenation
# print(msg,msg)  # Multiple arguments in print
# print(msg * 2)  # Repetition
# print(msg[0])   # Indexing
# print(msg[0:7]) # Slicing
# print(msg[-1])  # Negative indexing
# print(msg[-7:]) # Slicing with negative index
# print(msg[11:]) # Slicing from index 11 to end
# print(msg[11:15]) # Slicing from index 11 to 15
# print(msg[11:15:2]) # Slicing with step 2
# print(msg[::2])  # Slicing with step 2 from start to end
# print(msg[::-1]) # Reversing the string
# print(msg.count('o')) # Counting occurrences of 'o'
# print(msg.find('Python')) # Finding the index of 'Python'
# print(msg.index('Python')) # Finding the index of 'Python' (raises error if not found)
# print(msg.startswith('welcome')) # Checking if string starts with 'welcome'
# print(msg.endswith('Strings')) # Checking if string ends with 'Strings'
# print(msg.split()) # Splitting the string into a list of words
# print(msg.split(':')) # Splitting the string by ':'
# print(msg.split(' ')) # Splitting the string by space
# print(msg.split('o')) # Splitting the string by 'o'
# print(msg.strip()) # Stripping whitespace from both ends
# print(msg.lstrip()) # Stripping whitespace from the left
# print(msg.upper())  # Converting to uppercase
# print(msg.lower()) # Converting to uppercase and lowercase
# print(msg.capitalize()) # Capitalizing the first letter of the string
# print(msg.title()) # Capitalizing the first letter of each word (fails sometimes for instance when there is a number or apostrophe in the string)
# print(msg.replace('Python', 'Java'))    # Replacing 'Python' with 'Java'
# print(msg.find('Python'))       # Finding the index of 'Python' (returns -1 if not found)
# print(msg.rfind('Python'))      # Finding the last occurrence of 'Python'
# print(msg.index('Python'))     # Finding the index of 'Python' (raises error if not found)
# print(msg.split())      # Splitting the string into a list of words
# print(len(msg)) # Getting the length of the string



# String Exercise : Create a string from the string "Welcome to Python 101: Strings" extracting "1 Welcome Ring to Tyler" every first letter should be capitalized.
# Print the same string backwards.

# msg = "Welcome to Python 101: Strings"
# new_msg = msg[18] + " " + msg[0:7] + " " + msg[25:29] + " " + msg[8:10] + " " + msg[13] + msg [12] + msg[2] + msg [1] + msg[25]
# print(new_msg.title())
# reverse_msg = new_msg[::-1]
# print(reverse_msg.title())

# Multiline Strings
# msg = """Dear Terry,,
# You must cut down the mightiest 
# tree in the forest with…
# a herring! <3"""
# print(msg)


# msg  ='Welcome to Python 101: Strings'
# print(msg.find('h')) # Finding the index of 'h'
# print(msg.replace("Python", "Javascript")) # Replacing 'Python' with 'Javascript'
# print("Python" in msg) # Checking if 'Python' is in the string
# print("Python" not in msg) # Checking if 'Python' is not in the string


# name='TERRY'
# color = 'RED'
# msg = '[' + name + '] loves the color ' + color.lower() + '!'
# msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
# print(msg)
# print(msg1)

# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).
#
# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
#
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"

# My own solution
# user_total_time = x
# user_pit_stops = y
# user_avg_pit_time = z 
# z = x / y

# total_pit_time = user_pit_stops * user_avg_pit_time
# percentage_pit_time = (total_pit_time / user_total_time) * 100
# percentage_pit_time = round(percentage_pit_time, 2)
# print(f'Total pit stop time: {total_pit_time} seconds')

# The Right and Better solution
# Collect inputs
# total_race_time = float(input("Enter total race time (in seconds): "))
# num_pit_stops = int(input("Enter number of pit stops: "))
# avg_pit_duration = float(input("Enter average pit stop duration (in seconds): "))

# # Calculate total pit time
# total_pit_time = num_pit_stops * avg_pit_duration

# # Calculate pit time percentage
# pit_percentage = (total_pit_time / total_race_time) * 100
# pit_percentage = round(pit_percentage, 2)

# # Print results
# print("--- Pit Stop Summary ---")
# print(f"Total pit stop time: {total_pit_time} seconds")
# print(f"Percentage of race in pits: {pit_percentage}%")

# # Optional feedback
# if pit_percentage > 5:
#     print("You need a new pit crew. 🛠️")

# Lists

# friends = ['John','Michael','Terry','Eric','Graham']

# print(friends[1],friends[4])
# print(len(friends))
# print(friends.index("Eric"))
# print(friends.count('Eric'))
# cars = [911,130,328,535,740,308]
# print(friends)
# friends.sort()
# print(friends)
# friends.sort(reverse=True)
# print(friends)
# friends.reverse()             # Reversing
# print(friends)
# print(min(cars))            # Minimum            
# print(max(cars))              # Maximum  
# friends.append('Terry')     # Appending
# friends.insert(1,'Terry') # Inserting
# friends[2]='Terry' # Replacing
# friends.extend(cars) # Extending/adding two differnet lists
# friends.remove('Terry')
# # friends.remove[2] # Removing by value so wrong cos there is no 2
# friends.pop(-1) # Removing by index
# print(friends)
# friends.clear() # Clear the list
# del friends # Delete the list
# del friends[2] # Delete an index
# new_friends = friends[:]
# # or
# new_friends = friends.copy()
# # or
# new_friends = list(friends)
# print(friends)
# print(new_friends)

# List Excercise

# sales_w1 = [7,3,42,19,15,35,9]
# sales_w2 = [12,4,26,10,7,28]
# sales = []
# sales_w2.append(int(input("Enter today's sales: ")))
# sales = sales_w1 + sales_w2  # Concatenation of two lists
# # sales = sales_w1.extend(sales_w2) If you want to use extend, you should not assign it to a new variable because it returns none
# print(min(sales) * 1.5) 
# print(max(sales) * 1.5)
# print(min(sales) * 1.5 + max(sales) * 1.5) 


# # Correct code

# sales_w1a = [7,3,42,19,15,35,9]
# sales_w2a = [12,4,26,10,7,28]
# sales1 = []
# new_day = input('Enter #of lemonades for new day: ')
# sales_w2a.append(int(new_day))
# #sales.extend(sales_w1)
# #sales.extend(sales_w2)
# sales1 = sales_w1a + sales_w2a
# sales1.sort()
# worst_day_prof = min(sales1) * 1.5
# best_day_prof = max(sales1) * 1.5
# print(f'Worst day profit:$ {worst_day_prof}')
# print(f'Best day profit:$ {best_day_prof}')
# print(f'Combined profit:$ {worst_day_prof + best_day_prof}')

# Split and Join

# msg ='Welcome  to  Python  101: Split  and Join'
# csv = 'Eric,John,Michael,Terry,Graham'
# friends_list = ['Eric','John','Michael','Terry','Graham']
# print(msg.split()) # Default split by space does not consider multiple spaces
# print(msg.split(' '), type(msg.split(' '))) # Split by single space considers multiple spaces
# print(csv.split(',')) # Split by comma
# print(str(friends_list)) # Convert list to string but not a good way
# print('-'.join (friends_list)) # Join list elements with '-'
# print('-'.join(friends_list + friends_list)) # Join list elements with '-' and add first element at the end
# print(''.join(friends_list)) # Join list elements without any space
# print(''.join(msg.split())) # Join string elements without any space
# print(msg.replace (' ', '')) # Replace multiple spaces with single space

# Seperation Task
# csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
# print(','.join(csv.split(';')))
# print(','.join(csv.split(';')).split(':')) 
# print(','.join(','.join(csv.split(';')).split(':')))
# print(','.join(','.join(csv.split(';')).split(':')).split(','))

# # OR

# print('replace', csv.replace(';',',').replace(':',',').split(','))

# friends_list = ['Exercise: fill me with names']
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise
# print(csv.split(','))



#Tuples - faster Lists you can't change
friends = ['John','Michael','Terry','Eric','Graham']
friends_tuple = ('John','Michael','Terry','Eric','Graham')  #immutable
friends_set = {'Eric', 'John','Michael','Terry','Eric','Graham','Eric'}

print(friends)
print(friends_tuple)
print(friends_set)


