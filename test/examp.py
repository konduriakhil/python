class Pets:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def dog(self):
        print('Woof....')

    def cat(self):
        print('Meaow...')


class DomesticAnimals(Pets):
    def attributes(self):
        print('''             
Human friendly
Gives amusements to Humans 
Helps to Humans                            
''')


class Calculations:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def additon(self):
        return self.num1 + self.num2 
    
    def multiplication(self):
        return self.num1 * self.num2


def finding_max_no(numbers):
    max_no = numbers[0]
    for num in numbers:
        if num > max_no:
            max_no = num
    return max_no


def addition():
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    return num1 * num2


# dog1 = Pets('Maxi', 'Pumerian')
# dog2 = Pets('Jenduping', 'Desi')
# dog3 = DomesticAnimals('Hitler', 'BullDog')
# cat = Pets('Tiger', 'Bengal')


# print(dog1.name, dog1.breed)
# dog1.dog()

# dog2.name = 'Jinping'
# print(dog2.name, dog2.breed)
# dog2.dog()

# print(dog3.name, dog3.breed)
# dog3.dog()
# dog3.attributes()

# print(cat.name, cat.breed)
# cat.cat()