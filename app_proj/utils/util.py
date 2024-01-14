def format_message(use_uppercase, message, *args, **kwargs):
    formatted_message = message.format(*args, **kwargs)
    return formatted_message.upper() if use_uppercase else formatted_message

def calculate_sum(numbers):
    return sum(numbers)