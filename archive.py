import re
import math
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

class UserInputValidator:
    @staticmethod
    def contains_special_characters(string_data):
        pattern = r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\|]'
        return re.search(pattern, string_data) is not None

    @staticmethod
    def is_integer(string_data):
        try:
            int(string_data)
            return True
        except ValueError:
            return False

class UserDataProcessor:
    @staticmethod
    def get_valid_string_input(string_data):
        if string_data.lower() == 'exit':
            return None
        elif UserInputValidator.contains_special_characters(string_data):
            return 'Warning, the input should not contain special characters'
        elif UserInputValidator.is_integer(string_data):
            return f'The value "{string_data}" is not valid'
        else:
            return string_data

    @staticmethod
    def greetings(name):
        return f"My name is {name}"

    @staticmethod
    def high_school(name):
        return f"The name of my high school is {name}"

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        self.console_output = Label(text='', markup=True)
        self.result_label = Label(text='', markup=True)
        self.surname_input = TextInput(hint_text="Enter your surname (type 'exit' to quit)")
        self.name_input = TextInput(hint_text="Enter your name")
        self.school_input = TextInput(hint_text="Enter the name of your high school")
        self.height_input = TextInput(hint_text='Enter your height')
        self.weight_input = TextInput(hint_text='Enter your weight')
        self.submit_button = Button(text="Submit")
        self.submit_button.bind(on_release=self.process_input)

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(Label(text="Main Layout", font_size=24))
        layout.add_widget(Label(text="Surname:"))
        layout.add_widget(self.surname_input)
        layout.add_widget(Label(text="Name:"))
        layout.add_widget(self.name_input)
        layout.add_widget(Label(text="High School:"))
        layout.add_widget(self.school_input)
        layout.add_widget(Label(text='Height:'))
        layout.add_widget(self.height_input)
        layout.add_widget(Label(text='Weight:'))
        layout.add_widget(self.weight_input)

        layout.add_widget(Label())  # Spacer
        layout.add_widget(self.submit_button)
        layout.add_widget(self.result_label)
        layout.add_widget(self.console_output)

        self.add_widget(layout)

    def on_pre_enter(self):
        # Clear the result_label.text before entering the Main Layout
        self.clear_message_label()

    def clear_message_label(self):
        self.result_label.text = ''  # Clear the message label

    def process_input(self, instance):
        # Clear the result_label.text
        self.result_label.text = ''
        
        surname_string = self.surname_input.text.strip()
        name = self.name_input.text.strip()
        school = self.school_input.text.strip()
        height = self.height_input.text.strip()
        weight = self.weight_input.text.strip()

        if UserInputValidator.is_integer(surname_string) or UserInputValidator.is_integer(name) or UserInputValidator.is_integer(school):
            # Display the invalid values message in the result_label
            invalid_values = []
            if UserInputValidator.is_integer(surname_string):
                invalid_values.append(f'Surname ({surname_string})')
            if UserInputValidator.is_integer(name):
                invalid_values.append(f'Name ({name})')
            if UserInputValidator.is_integer(school):
                invalid_values.append(f'High School ({school})')

            if invalid_values:
                invalid_values_str = ', '.join(invalid_values)
                self.result_label.text = f'The following values are not valid: {invalid_values_str}'
            else:
                self.result_label.text = 'Height and Weight should be integers'
        elif not (height.isdigit() and weight.isdigit()):
            # Display a message if height or weight are not integers
            self.result_label.text = 'Height and Weight should be integers'
        else:
            # Check if other values are missing
            if not (name and surname_string and school):
                self.result_label.text = 'Missing values'
            else:
                # Calculate BMI
                height = int(height)
                weight = int(weight)
                bmi = (weight / ((height / 100) ** 2))

                surname_text = f"My surname is {surname_string.capitalize()}"
                full_text = ''

                # Check which values are entered and build the message accordingly
                if name:
                    full_text += UserDataProcessor.greetings(name)
                if surname_string:
                    full_text += f"{' and ' if full_text else ''}{surname_text}"
                if school:
                    full_text += f"{' and ' if full_text else ''}{UserDataProcessor.high_school(school)}"

                if full_text:
                    full_text += '\n'
                    self.add_to_console(full_text, 'bold magenta')
                    self.clear_input_fields()
                    self.result_label.text = "The following values are entered correctly:"
                    self.show_in_secondary(surname_string, name, school, height, weight, bmi)
                else:
                    self.add_to_console('No valid values entered', 'bold magenta')

    def add_to_console(self, text, style=''):
        current_text = self.console_output.text
        new_text = f'{current_text}{text}\n'
        self.console_output.text = f'[color={style}]{new_text}[/color]'

    def clear_input_fields(self):
        self.surname_input.text = ''
        self.name_input.text = ''
        self.school_input.text = ''
        self.height_input.text = ''
        self.weight_input.text = ''

    def show_in_secondary(self, surname, name, school, height, weight, bmi):
        secondary_screen = self.manager.get_screen('secondary')
        secondary_screen.update_labels(surname, name, school, height, weight, bmi)
        self.manager.current = 'secondary'

class SecondaryScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondaryScreen, self).__init__(**kwargs)

        self.secondary_label = Label(text="Secondary Layout", font_size=24)
        self.back_button = Button(text="Go Back to Main Layout")
        self.back_button.bind(on_release=self.go_to_main_layout)

        # Labels to display values from the Main layout
        self.surname_label = Label(markup=True)
        self.name_label = Label(markup=True)
        self.school_label = Label(markup=True)
        self.height_label = Label(markup=True)
        self.weight_label = Label(markup=True)
        self.bmi_label = Label(markup=True)  # Add BMI label

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(self.secondary_label)
        layout.add_widget(self.back_button)
        layout.add_widget(Label())  # Spacer
        layout.add_widget(self.surname_label)
        layout.add_widget(self.name_label)
        layout.add_widget(self.school_label)
        layout.add_widget(self.height_label)
        layout.add_widget(self.weight_label)
        layout.add_widget(self.bmi_label)  # Add BMI label

        self.add_widget(layout)

    def go_to_main_layout(self, instance):
        self.manager.current = 'main'

    def clear_message_label(self):
        self.surname_label.text = ''
        self.name_label.text = ''
        self.school_label.text = ''
        self.height_label.text = ''
        self.weight_label.text = ''
        self.bmi_label.text = ''

    def update_labels(self, surname, name, school, height, weight, bmi):
        self.clear_message_label()
        self.surname_label.text = f"[b]Surname:[/b] {surname.capitalize()}\n" if surname else ''
        self.name_label.text = f"[b]Name:[/b] {name}\n" if name else ''
        self.school_label.text = f"[b]High School:[/b] {school}\n" if school else ''
        self.height_label.text = f"[b]Height:[/b] {height} cm\n" if height else ''
        self.weight_label.text = f"[b]Weight:[/b] {weight} kg\n" if weight else ''
        self.bmi_label.text = f"[b]BMI:[/b] {bmi:.2f}\n" if bmi else ''

class ConsoleApp(App):
    def build(self):
        screen_manager = ScreenManager()

        main_screen = MainScreen(name='main')
        secondary_screen = SecondaryScreen(name='secondary')

        screen_manager.add_widget(main_screen)
        screen_manager.add_widget(secondary_screen)

        return screen_manager

if __name__ == "__main__":
    ConsoleApp().run()





