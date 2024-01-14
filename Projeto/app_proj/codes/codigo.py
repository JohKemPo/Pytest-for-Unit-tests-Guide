
import sys
sys.path.append('Projeto\app_proj')
from app_proj.utils.util import format_message, calculate_sum

class MyClass1:
    def __init__(self, name):
        self.name = name

    def greet(self, use_uppercase, *args, **kwargs):
        message = "Hello, {}!"
        formatted_message = format_message(use_uppercase, message, self.name)
        print(formatted_message.format(*args, **kwargs))

    def calculate_square(self, num):
        result = num ** 2
        print(f"The square of {num} is {result}")

class MyClass2:
    def __init__(self, value):
        self.value = value

    def display_info(self, use_uppercase, *args, **kwargs):
        message = "The value is {}."
        formatted_message = format_message(use_uppercase, message, self.value)
        print(formatted_message.format(*args, **kwargs))

    def calculate_cube(self, num):
        result = num ** 3
        print(f"The cube of {num} is {result}")
        
        
if __name__ == "__main__":
    obj1 = MyClass1("John")
    obj1.greet(True, "Have a nice day!")

    obj2 = MyClass2(10)
    obj2.display_info(False, "Additional info")

    numbers = [1, 2, 3, 4, 5]
    sum_result = calculate_sum(numbers)
    print(f"Sum of numbers: {sum_result}")

    obj1.calculate_square(4)
    obj2.calculate_cube(3)