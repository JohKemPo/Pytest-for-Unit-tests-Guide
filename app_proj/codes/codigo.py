
import sys
# comando usado para adicionar o caminho do projeto ao path do python, assim o pytest consegue encontrar os módulos. Fazer somente se houver erro ao encontrar o módulo.
sys.path.append('~/Pytest-for-Unit-tests-Guide/')
from app_proj.utils.util import format_message, calculate_sum

class MyClass1:
    def __init__(self, name):
        self.name = name

    def greet(self, use_uppercase: bool, *args, **kwargs):
        message = "Hello, {}!"
        formatted_message = format_message(use_uppercase, message, self.name)
        print(formatted_message.format(*args, **kwargs))

    def calculate_square(self, num: int | float):
        result = num ** 2
        print(f"The square of {num} is {result}")

class MyClass2:
    def __init__(self, value: int | float):
        self.value = value

    def display_info(self, use_uppercase: bool, *args, **kwargs):
        message = "The value is {}."
        formatted_message = format_message(use_uppercase, message, self.value)
        print(formatted_message.format(*args, **kwargs))

    def calculate_cube(self, num: int | float):
        result = num ** 3
        print(f"The cube of {num} is {result}")
        
'''
    Trecho de código para testar o funcionamento do código.
    
    IMPORTANTE: Comente o trecho abaixo antes de executar os testes.
    
                É importante ter conhecimento de dado um input o como
                o código se comporta para planejar as fixtures usados nos testes.
'''        

# if __name__ == "__main__":
#     obj1 = MyClass1("John")
#     obj1.greet(True, "Have a nice day!")

#     obj2 = MyClass2(10)
#     obj2.display_info(False, "Additional info")

#     numbers = [1, 2, 3, 4, 5]
#     sum_result = calculate_sum(numbers)
#     print(f"Sum of numbers: {sum_result}")

#     obj1.calculate_square(4)
#     obj2.calculate_cube(3)