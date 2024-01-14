from app_proj.utils.util import format_message, calculate_sum

# Tests for utils.py
def test_format_message():
    assert format_message(True, "Hello, {}!", "John") == "HELLO, JOHN!"
    assert format_message(False, "Hi, {}!", "Alice") == "Hi, Alice!"

def test_calculate_sum():
    numbers = [1, 2, 3, 4, 5]
    assert calculate_sum(numbers) == 15
    assert calculate_sum([]) == 0