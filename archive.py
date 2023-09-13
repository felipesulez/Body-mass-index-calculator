from rich import print
from rich.console import Console
import re

console = Console()
flag = False

def contains_special_characters(string_data):
    pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\|]'
    return re.search(pattern, string_data) is not None

def greetings(name):
    return f"My name is {name}"

def input_string(prompt):
    user_input = input(prompt)
    return user_input

def name_input():
    global flag  # Declare flag as a global variable

    name = input_string("\nEnter your name: ")
    school = input_string("Enter the name of your high school: ")
        
    try: 
        value1 = int(name)
        value2 = int(school)

        console.print(f'Warning, {value1} and {value2} are integers', style='bold magenta')
        flag = False
        return value1, value2

    except ValueError:
        print(f"{name} and {school} are strings")
        flag = True
        return name, school

def high_school(name):
    return f"The name of my high school is {name}"

def main():
    def surname(surname_string):

        try: 
            surname = int(surname_string)
            console.print(f'\n {surname} is not', 
                          'a string', style='bold red')
        except ValueError:
            console. print(f'\n {surname} is a valid',
                           'string', style='bold green')
            name, school = name_input()
            surname_text = f"My surname is {surname_string}"
            if flag:
                full_text = f"{greetings(name)} and {surname_text} and {high_school(school)}\n"
                console.print("Calling the name_input function", style="bold magenta")
                return full_text
            else:
                print('These values are not strings')
                return None
            
    print(surname(input("\nEnter your surname: ")))

if __name__ == "__main__":
    main()
