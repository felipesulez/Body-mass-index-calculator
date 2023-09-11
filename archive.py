from rich import print
from rich.console import Console

console = Console()

def greetings(name):
    return f"My name is {name}"

def name_input():
    
    name = input("\nEnter your name: ")
    school = input("Enter the name of your high school: ")
    console.print(name, school, style="bold green")
    return name, school

def high_school(name):
    return f"The name of my high school is {name}"

def main():

    def surname(surname_string):
        name, school = name_input()
        surname_text = f"My surname is {surname_string}"
        full_text = f"{greetings(name)} and {surname_text} and {high_school(school)}\n"
        console.print("Calling the name_input function", style="bold magenta")
        name_input()
        return full_text

    print(surname(input("\nEnter your surname: ")))

if __name__ == "__main__":
    main()






