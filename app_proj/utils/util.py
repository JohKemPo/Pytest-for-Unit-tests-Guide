def format_message(use_uppercase: bool, message: str, *args, **kwargs):
    formatted_message = message.format(*args, **kwargs)
    return formatted_message.upper() if use_uppercase else formatted_message

def calculate_sum(numbers: list):
    return sum(numbers)