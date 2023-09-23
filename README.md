# Body-mass-index-calculator

Body Mass Index (BMI) Calculator
BMI Calculator

This is a simple BMI calculator app built using the Kivy framework in Python. The app allows users to input their personal information such as name, surname, high school, height, and weight, and then calculates their BMI based on these inputs.

How to Use
Enter your surname.
Enter your name.
Enter the name of your high school.
Enter your height in centimeters.
Enter your weight in kilograms.
Click the "Submit" button.
The app will then process your input and provide you with the following information:

Your entered values, including surname, name, high school, height, and weight.
Your calculated BMI (Body Mass Index).
Features
Input validation to ensure that only valid numerical values are entered for height and weight.
Robust validation to prevent integers from being entered as names or high school names.
BMI calculation based on the entered height and weight.
A secondary screen that displays the entered values and BMI result with a BMI status (underweight, healthy weight, overweight, or obesity).

## BMI Categories

The app categorizes your BMI result into the following categories:

- **Underweight:** BMI less than 18.5
- **Healthy Weight:** BMI between 18.5 and 24.9
- **Overweight:** BMI between 25.0 and 29.9
- **Obesity:** BMI 30.0 or greater

## Screenshots

![Main Screen](screenshots/Main.png)

![Secondary Screen](screenshots/Second.png)

## Dependencies

- Kivy: The app is built using the Kivy framework for the graphical user interface.
- Python: The app is written in Python 3.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/felipesulez/Body-mass-index-calculator.git

2. Install the required dependencies:
   ```bash
   pip install kivy

3. Run the app:
    ```bash
    python archive.py
    
## Author

Felipe Antonio Sulez Gomez 

## License

This project is licensed under the MIT License. See the LICENSE.md file for details.
