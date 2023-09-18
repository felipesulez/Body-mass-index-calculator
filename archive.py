from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import re

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
            return 'The values Surname, Name, and High School are not valid'
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
        self.submit_button = Button(text="Submit")
        self.submit_button.bind(on_release=self.process_input)
        self.secondary_button = Button(text="Go to Secondary Layout")
        self.exit_button = Button(text = 'Exit')
        self.secondary_button.bind(on_release=self.go_to_secondary_layout)

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(self.surname_input)
        layout.add_widget(self.name_input)
        layout.add_widget(self.school_input)
        layout.add_widget(self.submit_button)
        layout.add_widget(self.exit_button)

        layout.add_widget(self.secondary_button)
        layout.add_widget(self.result_label)
        layout.add_widget(self.console_output)

        self.add_widget(layout)

    def process_input(self, instance):
        # Clear the result_label.text
        self.result_label.text = ''
        
        surname_string = self.surname_input.text.strip()
        name = self.name_input.text.strip()
        school = self.school_input.text.strip()

        if UserInputValidator.is_integer(surname_string) or UserInputValidator.is_integer(name) or UserInputValidator.is_integer(school):
            # Display the invalid values message in the result_label
            self.result_label.text = 'The values Surname, Name, and High School are not valid'
        else:
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
                self.result_label.text = "The following values are entered correctly: "
                if name:
                    self.result_label.text += "Name, "
                if surname_string:
                    self.result_label.text += "Surname, "
                if school:
                    self.result_label.text += "High School, "
                self.result_label.text = self.result_label.text.rstrip(", ")  # Remove trailing comma
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

    def go_to_secondary_layout(self, instance):
        self.manager.current = 'secondary'

class SecondaryScreen(Screen):
    def __init__(self, **kwargs):
        super(SecondaryScreen, self).__init__(**kwargs)

        self.secondary_label = Label(text="This is the Secondary Layout")
        self.back_button = Button(text="Go Back to Main Layout")
        self.back_button.bind(on_release=self.go_to_main_layout)

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(self.secondary_label)
        layout.add_widget(self.back_button)

        self.add_widget(layout)

    def go_to_main_layout(self, instance):
        self.manager.current = 'main'

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
