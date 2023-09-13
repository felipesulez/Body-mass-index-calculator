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
    while True:
        name = input("\nEnter your name: ")
        school = input("Enter the name of your high school: ")

        if contains_special_characters(name) or contains_special_characters(school):
            console.print('Warning, name and school should not contain special characters', style='bold magenta')
        elif name.isdigit() or school.isdigit():
            console.print('Name and school should not be integers', style='bold magenta')
        else:
            console.print(f"\n {name} and {school} are strings",
                          style='bold green')
            return name, school

def high_school(name):
    return f"The name of my high school is {name}"

def main():
    surname_string = input("\nEnter your surname: ")

    try:
        surname = int(surname_string)
        console.print(f'\n {surname} is not a string', style='bold red')
    except ValueError:
        console.print(f'\n {surname_string} is a valid string', style='bold green')
        name, school = name_input()
        if name and school:
            surname_text = f"My surname is {surname_string}"
            full_text = f"{greetings(name)} and {surname_text} and {high_school(school)}\n"
            #console.print("Calling the name_input function", style="bold magenta")
            console.print(f'\n {full_text}', 
                  style = 'bold magenta')
        else:
            print('These values are not strings')

if __name__ == "__main__":
    main()


