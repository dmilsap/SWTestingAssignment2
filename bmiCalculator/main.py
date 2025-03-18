# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import bmiCalculator, string


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
        weight = float(input("Please enter you weight in pounds: "))
        feet = int(input("Please enter your height(feet): "))
        inches = int(input("Please enter your height(inches): "))
        bmi = bmiCalculator.calculateBMI(weight, feet, inches)
        category = bmiCalculator.outputBMICategory(bmi)
        print (bmi)
        while(True):
            answer = str(input("Do you want to continue? Y or N\n"))
            if answer == "Y":
                weight = float(input("Please enter you weight in pounds: "))
                feet = int(input("Please enter your height(feet): "))
                inches = int(input("Please enter your height(inches): "))
                bmi = bmiCalculator.calculateBMI(weight, feet, inches)
                category = bmiCalculator.outputBMICategory(bmi)
                print(bmi)
            elif answer == "N":
                break

            else:
                print("Invalid input! Enter N or Y")





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
