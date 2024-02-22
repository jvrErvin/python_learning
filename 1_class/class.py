# 1: Intro, oop, class, object
class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def bark(self):
        return f"Woof! My name is {self.name} and I am {self.age} years old. "
    
    def duplicate_age(self):
        self.age *= 2
        if self.age >= 10:
            self.old = True
            

# 2: Inheritance
class Animal:
    def __init__(self, species: str):
        self.species = species
        
    def make_sound(self):
        pass


class Cat(Animal):
    def __init__(self, name: str):
        super().__init__("Cat")
        self.name = name
        
    def make_sound(self):
        return "Meow!"
    
    
class Squirrel(Animal):
    def __init__(self, name: str):
        super().__init__("Squirrel")
        self.name = name
    
    
# 3: Encapsulation
class Computer:
    def __init__(self):
        self.__max_price = 900  # private
    
    # Setter
    def set_max_price(self, price):
        self.__max_price = price
    
    # Getter
    def get_max_price(self):
        return self.__max_price
        

# 4: Polymorphism
class Circle:
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
    
class Rectangle:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
        
    def area(self):
        return self.a * self.b


def area():
    return "Yuhuu"

def area():
    return 42

# 5: Special methods
class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"{self.title} by {self.author}, number of pages: {self.pages}"
    
    def __repr__(self):
        return f"{self.title!r}, {self.author!r}, {self.pages!r} ASD"
    
class Libray:
    def __init__(self):
        self.books = []
        
    def add_book(self, book: Book):
        self.books.append(book)
    
    def __len__(self):
        return len(self.books)
    
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)



if __name__ == "__main__":
    # 1: Intro, oop, class, object
    bob = Dog("Bob", 5)
    polly = Dog("Polly", 3)
    
    print(bob.bark())
    
    # 2: Inheritance
    elfy = Cat("Elfy")
    mogyi = Squirrel("Mogyi")
    
    # 3: Encapsulation
    comp = Computer()
    
    # 4: Polymorphism
    circle = Circle(5)
    rectangle = Rectangle(3, 4)
    
    print(circle.area())
    print(rectangle.area())
    print(area())
    
    # 5: Special methods
    random_book = Book("Random Book", "Random Author", 42)
    print(random_book) # random_book.__str__() -- str(random_book)
    print(repr(random_book))
    
    random_library = Libray()
    random_library.add_book(random_book)
    random_library.add_book(Book("Random Book 2", "Random Author 2", 43))
    print(len(random_library)) # random_library.__len__() -- len(random_library)
    
    p1 = Point(1,2)
    p2 = Point(3,4)
    p3 = p1 + p2
    p4 = p1 - p2
    print(p3.x, p3.y)
    print(p4.x, p4.y)
    
    a = 1
    