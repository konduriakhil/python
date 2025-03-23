# Weight converter from kgs to pounds
weight_in_kg = input('Enter your weight in kgs: ')
weight_in_pounds = float(weight_in_kg) * 2.205
print(f'Your weight in Pounds: {weight_in_pounds:.2f} ')

# Weight converter from pounds to kgs
weight_in_pounds = input('Enter your weight in pounds: ')
weight_in_kgs = float(weight_in_pounds) / 2.205
print(f'Your weight in kgs: {weight_in_kgs:.2f} ')

# Type conversion (Finding the age)
birth_year = int(input('Enter your birth year: '))
print(type(birth_year))
age = 2025 - birth_year
print(f'Your age is: {age}')


# Formated String
first_name = 'Konduri'
last_name = 'Akhil'
message = f'{first_name} [{last_name}] is a learner'
print(message)

# Lenght of a string
course = 'This is python learning Program'
print(len(course))

# Changing to uppercase
course = 'This is python learning Program'
print(len(course))
print(course.upper())

# Lower case
course = 'This is python learning Program'
print(len(course))
print(course.lower())

# Finding index of a character or word
course = 'This is python learning Program'
print(len(course))
print(course.lower())
print(course.find('i'))
print(course.find('python'))
print(course.find('python', 'is'))  #Output: TypeError: must be str, not str


# Multiplication 
num1 = input('enter first number: ')
num2 = input('enter second number: ')
result = int(num1) * int(num2)
print(f'The result of multiplication is: {result}')

# If statement (Day situation)
is_hot = True
if is_hot:
    print('''
          It is a hot day,
          Drink plenty of water.
    ''')
else:
    print('''
    It is a cold day,
    Wear warm cloths.
''')
print('Enjoy your day.')


is_hot = True
is_cold = True
if is_hot:
    print('''
          It is a hot day,
          Drink plenty of water.
    ''')
elif is_cold:
    print('''
        It is a cold day,
        Wear warm cloths.
''')
else:
    print('''
        Its a lovely Day.
''')
print('Enjoy your day.')


# Small exercise(Discounting to customers)
price_of_house = 100
rich_customer = False
final_price = 0
if rich_customer:
    final_price = 100 - (10/100 * 100)
    print(f'The price of the house is : {final_price}')
else: 
    final_price = 100 - (20/100 * 100)
    print(f'The price of the house is : {final_price}')


# Logical operators
has_degree = True
has_certificate = False
if has_degree and has_certificate:
    print('This application is eligible for job')
else:
    print('This application is not eligible for job')


has_degree = True
has_certificate = True
has_criminal_record = False
if has_degree and not has_criminal_record:
    print('This application is eligible for job')
else:
    print('This application is not eligible for job')

    # Day temparature
temparature = int(input('Enter temparature: '))
if temparature > 30:
    print('It is hot day')
elif temparature < 20:
    print('It is a cold day')
else:
    print('It is a nice day')

    # Name character correction
name = input('Enter the name: ')
if len(name) < 3:
    print('Length of your name is: ' + str(len(name)))
    print('Length of the name must contain minimum of 3 characters')
elif len(name) > 50:
    print('Length of your name is: ' + str(len(name)))
    print('Length of the name must not exceed 50 characters')
else:
    print('Thank You for giving your name.')

#Weight: 
    # (L)bs or (K)g: 
    # You are 160.0 pounds
weight = float(input('Enter your weight in kgs : '))
choice = input('(K)gs or (L)bs: ')
lbs = 0 
if choice == 'K' or choice == 'k':
    print(f'Your weight in Kgs: {weight}' + ' kgs')
elif choice == 'L' or choice == 'l':
    lbs = weight * 2.205 
    print(f'Your weight in Lbs: {lbs:.2f}' + ' lbs')
else:
    print('You entered wrong option')

# While Loops
    # if = "If this is true, do this (once)."
    # while = "While this is true, keep doing this."

i = 1
while i <= 100:
    print(i)
    i = i + 1
print('Done')


i = 1
while i <= 99:
    print('*' * i)
    i = i + 1
print('Done')

    # Number guessing game
guess_count = 0
guess_limit = 3
secret = 9
while guess_count < guess_limit:
    guess = int(input('Guess the number: '))
    guess_count = guess_count + 1
    if guess == secret:
        print('You Won!')
        break
else: 
    print('You Lost')


    # Number Guessing Version-2
number = 3
no_of_guesses = 0
max_no_of_chances = 3
while no_of_guesses < 3:
    user_number = int(input('Enter your number: '))
    if user_number == number:
        print('You are right')
        break
    elif user_number != number:
        print('Your guess is wrong')
        no_of_guesses += 1
        no_of_chances_left = max_no_of_chances - no_of_guesses
        print(f'no of chances left: {no_of_chances_left}')
    else:
        print('You enterd wrong input')
print('Bye')        

    # Car game version-1
command = ''
start = ''
stop = ''
while True:
    command = input('> ').lower()
    if command == 'start':
        if start == '':
            print('Car is started')
            start = 'start'
        else:
            print('Car is already started')
    elif command == 'stop':
        if stop == '':
            print('Car is stopped')
            stop = 'stop'
        else:
            print('car is already stopped')
    elif command == 'help':
        print('''
start - To start the car
stop - To stop the car 
quit - To quit the game
''')
    elif command == 'quit':
        print('Quitted')
        break
    else:
        print("I don't understand")

    # Car game version-2
command = ''
started = False
stopped = False
while True:
    command = input('Enter your input: ')
    if command == 'start':
        if started:
            print('Car is already started')
            stopped = False
        else:
            print('Car is started...Ready to go...🏎️')
            started = True
            stopped = False
    elif command == 'stop':
        if stopped:
            print('Car is already stopped')
            started = False
        else:
            print('Car is stopped')
            stopped = True
            started = False

    elif command == 'quit':
        print('You quitted the game')
        break
    elif command == 'help':
        print('''
start - to start the car
stop - to stop the car                
quit - to quit from game              
''')
    else:
        print("You entered wrong command, enter 'help' for the help")
print('Thank You for your time')

# For loops

for item in 'Konduri Akhil': # here 'item' is variable and is being set to different characters of Konduri Akhil and get printed for iterations.
    print(item)

for item in ['K Venkateswarlu', 'K Vasantha', 'K Akhil', 'K Sai Varshath']:
    print(item)

for item in ['Konduri Venkateswarlu', 'Konduri Vasantha', 'Konduri Akhil', 'Konduri Sai Varshath']:
    print(item)
    
for item in range(10):
    print(item)

for item in range(5, 10):
    print(item)

for x in range(5, 10, 2): # In the Python code for x in range(5, 10, 2): print(x), the number 2 represents the step value within the range() function, So, it will iterate through the numbers by adding 2 each time.
    print(x)

    # Print total
prices = [10, 20, 30, 40]
total = 0
for price in prices:
    total += price
print(f'The total price is: {total}')

# Nested Loops(calling one loop in other loop)

for x in range(2):
    for y in range(3):
        print(f'({x}, {y})')

    # Printing F symbol using for loop
numbers = [5, 2, 5, 2, 2]
for x in numbers:
    output = ''
    for y in range(x):
        output += 'x'
    print(output)

    # Printing L shape by using for loop
numbers = [2, 2, 2, 2, 8]
for x in numbers:
    output = ''
    for y in range(x):
        output += 'x'
    print(output) 

# Lists

names = ['Akhil', 'Sai', 'Varshath', 'India', 'Pakistan']
print(names[-1])
print(names[0])
print(names[2:])
print(names[0])
print(names[2:4])
print(names[:])

names = ['Akhil', 'Sai', 'Varshath', 'India', 'Pakistan']
names[0] = 'Konduri Akhil'
print(names)

    # Finding the largest number in a list
items = [23, 34, 7, 97683, 47787873, 73]
largest = items[0]
for x in items:
    if x > largest:
        largest = x
print(f'The largest number is {largest}')


# 2D List (2 diementional list) 
    # In this each item in list represents other list.

matrix = [ 
    [1, 2, 3],
    [4, 5, 61],
    [7, 8, 9] 
    ]
print(matrix[0][2])


matrix = [ 
    [1, 2, 3],
    [4, 5, 61],
    [7, 8, 9] 
    ]
for x in matrix:
    print(x)

matrix = [ 
    [1, 2, 3],
    [4, 5, 61],
    [7, 8, 9] 
    ]
for row in matrix:
    for item in row:
        print(item)

# List Methods

numbers = [23, 34, 7, 97, 683, 47, 78, 78, 73, 73]
numbers.append(87)
print(numbers)

numbers = [23, 34, 7, 97, 683, 47, 78, 78, 73, 73]
numbers.insert(0, 87)# first is index and send is actual object.
print(numbers)

numbers = [23, 34, 7, 97, 683, 47, 78, 78, 73, 73]
numbers.remove(97)
print(numbers)

numbers = [23, 34, 7, 97, 683, 47, 78, 78, 73, 73]
numbers.clear() # To clear all the objects
print(numbers)

numbers = [23, 34, 7, 97, 683, 47, 78, 78, 73, 73]
numbers.pop() # To remove last object
print(numbers)

numbers = [23, 34, 7, 97, 683, 47, 78, 78, 73, 73]
print(numbers.index(34))# to know index of particular number

numbers = [23, 34, 7, 97, 683, 47, 78, 78, 73, 73]
print(50 in numbers)

numbers = [23, 34, 7, 97, 683, 47, 78, 78, 73, 73]
numbers2 = numbers.copy()
numbers2.sort()
print(numbers)
print( numbers2 )

    # To remove duplicates in a list
numbers = [23, 34, 7, 97, 683, 47, 78, 78, 73, 73]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
print(numbers)

# Tuples (these are list's that are immutable, we can not change tuples)

numbers = (23, 34, 7, 97, 683, 47, 78, 78, 73, 73)
# numbers[0] = 10
print(numbers)

coordinates = (1, 2, 3)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
print(x)


# or 

coordinates = (1, 2, 3)
x, y, z = coordinates
print(x)

# Dictionaries (To store information in key-value pair)

customer = {
    'name': 'Konduri Akhil',
    'age': 27,
    'is_married': False
}
print(customer['name'])
print(customer['age'])

customer = {
    'name': 'Konduri Akhil',
    'age': 27,
    'is_married': False
}
print(customer['guardian'])

customer = {
    'name': 'Konduri Akhil',
    'age': 27,
    'is_married': False
}
print(customer.get('guardian'))

customer = {
    'name': 'Konduri Akhil',
    'age': 27,
    'is_married': False
}
print(customer.get('guardian', 'Venkateswarlu'))

customer = {
    'name': 'Konduri Akhil',
    'age': 27,
    'is_married': False
}
customer['name'] = 'Akhil'
print(customer['Date Of Birth'])

customer = {
    'name': 'Konduri Akhil',
    'age': 27,
    'is_married': False
}
customer['Date Of Birth'] = '21/06/1998'
print(customer['Date Of Birth'])
 
    # Converting number into digits
mobile = input('Enter your mobile no: ')
digital_form = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '0': 'zero'
}
output = ''
for ch in mobile:
    output += digital_form.get(ch, '!') + ' '
print(output)

message = input('Enter the message: ')
words = message.split(' ')
print(words)

    # Emoji Converter
message = input('Enter the message: ')
words = message.split(' ')
emojis = {
    ':)': '😊', # windows + ;
    ':(': '😒'
}
output = ''
for word in words:
    output += emojis.get(word, word) + ' '
print(output)

# Functions

def greet_Hari():
    print('Hi, Hari')
    print('How are you?')

print('Texting to Hari.')
greet_Hari()
print('Texting to Hari is ended.')

# Parameters

def greeting_user(name):
    print(f'Hi, {name}')
    print('How are you?')

greeting_user('Hari')
greeting_user('Sai')

# Positional arguments

def greeting(name, village):
    print(f'''
hi {name}
how are you?
when will you come to {village}?
''')
greeting('hari', 'martur')        
greeting('sai', 'bangalore')

# Keyword Arguments
    # If you want to use both positonal and keyword argument 
        # First use positional argument and last use keyword argument

def greeting_user(first_name, second_name):
    print(f'Hi, {first_name} {second_name}')
    print('How are you?')

print('Texting to users')
greeting_user(second_name='Hari', first_name='Sivarathri')
greeting_user('Sai', 'Konduri')
print('Texting to users is ended')

# Return statement
def calculation(number):
    return number * number
print(calculation(6))

def calculation(number):
    print( number * number)# without return statement it assumes return default value as none
print(calculation(6))

# Creating reusable function
    # Base Function
message = input('Enter your message: ')
words = message.split(' ')
emoji = {
    ':)': '😊',
    ':(': '😒'
}
output = ''
for word in words:
    output += emoji.get(word, word) + ' '
print(output)

    # Reusable Function
def emoji_converter(message):
    words = message.split(' ')
    emoji = {
        ':)': '😊',
        ':(': '😒'
    }
    output = ''
    for word in words:
        output += emoji.get(word, word) + ' '
    return output
message = input('Enter your message: ')
print(emoji_converter(message))

# Exceptions

try:
    age = int(input('Enter your age: '))
    print(age)
except ValueError:
    print('Invalid code')

try:
    age = int(input('Enter your age: '))
    experience = 100
    meturity = experience / age
    print(age)
except ZeroDivisionError:
    print('age can not be 0')
except ValueError:
    print('Invalid code')

# Comments( We use # for commenting )

# Classes
    # The naming convention of variables and functions are lowercase letters and separte them using underscore
        # def multiplication_of_two_numbers(), number = 2, name_of_person = 'Akhil'
    # For Classes start with uppercase letter and separation is start with Uppercase letter
        # class PointInGame


    # Program-1
class Dog:  # The recipe (class) for making dog objects
    def __init__(self, name, breed): #ingredients of the dog (init method is run when dog is created)
        self.name = name
        self.breed = breed

    def bark(self): #step of the recipe (method)
        print("Woof!")

my_dog = Dog("Buddy", "Golden Retriever")  # Making a dog (object) using the recipe
your_dog = Dog("Max", "Poodle") # Making another dog (object)

print(my_dog.name)  # Accessing the dog's name (an ingredient)
my_dog.bark()  # Making the dog bark (using a step of the recipe)

print(your_dog.name)
your_dog.bark()    

    # Program-2
class School:
    def teachers(self):
        print('teachers')

    def students(self):
        print('students')


school1 = School()
school1.x = 16
school1.y = 100
school1.teachers()
print(school1.x)
school1.students()
print(school1.y)


school2 = School()
school2.x = 28
school2.y = 250
school2.teachers()
print(school2.x)
school2.students()
print(school2.y)

