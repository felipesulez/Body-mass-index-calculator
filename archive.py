from rich import print
from rich.console import Console
import re

console = Console()

def contains_special_characters(string_data):
    pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\|]'
    return re.search(pattern, string_data) is not None

def greetings(name):
    return f"My name is {name}"

def input_string(prompt):
    user_input = input(prompt)
    return user_input

def name_input():
    try: 
        name = input_string("\nEnter your name: ")
        school = input_string("Enter the name of your high school: ")

        if contains_special_characters(name):
            console.print(f'\nThere is at least one special character', style='bold red')
        elif contains_special_characters(school):
            console.print(f'\nThere is at least one special character in', style='bold red')

        return name, school

    except ValueError as e:
        print(e)

def high_school(name):
    return f"The name of my high school is {name}"

def main():
    def surname(surname_string):
        name, school = name_input()
        surname_text = f"My surname is {surname_string}"
        full_text = f"{greetings(name)} and {surname_text} and {high_school(school)}\n"
        console.print("Calling the name_input function", style="bold magenta")
        return full_text

    print(surname(input("\nEnter your surname: ")))

if __name__ == "__main__":
    main()



