# 1. Write a Program to implement destructor and constructors using __del__() and __init__()

class Car :

    # constructor
    def __init__(self, user_brand, user_model) :
        self.brand = user_brand
        self.model = user_model

    # destructor
    def __del__(self) :
        print(f"Deleting {self.brand} {self.model} instance")

# creating an instance of the car
my_car = Car("Tata", "Safari")

print(my_car.model)
print(my_car.brand)


print()








# 2. Write a Program to implement Getters and Setters in a class

class Car :

    # constructor
    def __init__(self, user_brand, user_model) :     
        self.__brand = user_brand   # __ makes the attribute private, encapsulation
        self.model = user_model

    # getter 
    def get_brand(self) :
        return self.__brand
    
    # setter
    def set_brand(self, new_brand) :
        self.__brand = new_brand
    

my_car = Car("Toyota", "Corolla") 

print(my_car.model)
my_car.set_brand("Honda")
print(my_car.get_brand())


print()









# 3. Write a Program to calculate student grade using class

class Student :

    def __init__(self, name, marks) :
        self.name = name
        self.marks = marks

    def calculateGrade(self) :
        avg_marks = sum(self.marks) / len(self.marks)

        if (avg_marks >= 90) :
            return 'A+'

        elif (avg_marks >= 80) :
            return 'B'

        elif (avg_marks >= 70) :
            return 'C'

        elif (avg_marks >= 60) :
            return 'D'
        
        else :
            return "Fail"


student_name = input("Enter student's name : ")
subjects = int(input("Enter the number of subjects : "))
marks = []

for i in range(subjects) :
    score = float(input(f"Enter marks for the {i+1}'s subject : "))
    marks.append(score)


student = Student(student_name, marks)

grade = student.calculateGrade()

print(f"{student_name}'s grade is {grade}")


print()








# 4. Write a Program to illustrate single inheritance in Python

class Animal :
    def __init__(self, name) :
        self.name = name

    def speak(self) :
        print (f"{self.name} is an animal.")
    

class Cat(Animal) : 
    def __init__(self, name, breed) :
        super().__init__(name)
        self.breed = breed
    
    def speak(self) :
        super().speak()
        print (f"{self.name} meows")


animal = Animal("My cat")
animal.speak()

cat = Cat("kitty", "Persian Cat")
cat.speak()

print()








# 5. Write a Program to illustrate multiple inheritance in Python

class Animal :
    def __init__(self, name) :
        self.name = name

    def speak(self) :
        print (f"{self.name} meows.")


class Pet :
    def __init__(self, name, owner) :
        self.name = name 
        self.owner = owner

    def sleep(self) :
        print(f"{self.name} is sleeping.") 


class Cat(Animal, Pet) : 
    def __init__(self, name, owner) :
        Animal.__init__(self, name)
        Pet.__init__(self, name, owner)
    
    def play(self) :
        print(f"{self.name} is playing with {self.owner}.")


my_cat = Cat("kitten", "khushi")

my_cat.speak()
my_cat.sleep()
my_cat.play()


print()








# 6. Write a Program to illustrate multilevel inheritance in Python

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is an animal.")


class Pet(Animal):
    def __init__(self, name, owner):
        # Call the constructor of the base class (Animal)
        super().__init__(name)
        self.owner = owner

    def describe(self):
        print(f"{self.name} is owned by {self.owner}.")


class Cat(Pet) :
    def __init__(self, name, owner):
        # Call the constructor of its base class (Pet)
        super().__init__(name, owner)

    def play(self):
        print(f"{self.name} is playing with the ball.")


my_cat = Cat("kitten", "khushi")

my_cat.speak()
my_cat.describe()
my_cat.play()