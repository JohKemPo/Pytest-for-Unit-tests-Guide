# test_main.py
from app_proj.codes.codigo import MyClass1, MyClass2
import pytest



# Tests for main.py
def test_myclass1_greet(capsys):
    obj = MyClass1("John")
    obj.greet(True, "Have a nice day!")
    captured = capsys.readouterr()
    assert captured.out.strip() == "HELLO, JOHN!"

def test_myclass1_calculate_square(capsys):
    obj = MyClass1("John")
    obj.calculate_square(4)
    captured = capsys.readouterr()
    assert captured.out.strip() == "The square of 4 is 16"

def test_myclass2_display_info(capsys):
    obj = MyClass2(10)
    obj.display_info(False, "Additional info")
    captured = capsys.readouterr()
    assert captured.out.strip() == "The value is 10."

def test_myclass2_calculate_cube(capsys):
    obj = MyClass2(10)
    obj.calculate_cube(3)
    captured = capsys.readouterr()
    assert captured.out.strip() == "The cube of 3 is 27"
