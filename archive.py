

from rich.console import Console
import re

console = Console()

def contains_special_characters(string_data):
    pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\|]'
    return re.search(pattern, string_data) is not None

def is_integer(string_data):
    try:
        int(string_data)
        return True
    except ValueError:
        return False

def get_valid_string_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'exit':
            return None
        elif contains_special_characters(user_input):
            console.print('Warning, the input should not contain special characters', style='bold magenta')
        elif is_integer(user_input):
            console.print('The input should not be an integer', style='bold magenta')
        else:
            return user_input

def greetings(name):
    return f"My name is {name}"

def high_school(name):
    return f"The name of my high school is {name}"

def main():
    while True:
        surname_string = input("\nEnter your surname (type 'exit' to quit): ")
        if surname_string.lower() == 'exit':
            break
        try:
            int(surname_string)
            console.print(f'\n {surname_string} is not a string', style='bold red')
        except ValueError:
            name = get_valid_string_input("\nEnter your name: ")
            school = get_valid_string_input("Enter the name of your high school: ")
            if name is not None and school is not None:
                surname_text = f"My surname is {surname_string.capitalize()}"
                full_text = f"{greetings(name)} and {surname_text} and {high_school(school)}\n"
                console.print(f'\n{full_text}', style='bold magenta')
        else:
            console.print('These values are not strings', style='bold magenta')

if __name__ == "__main__":
    main()

