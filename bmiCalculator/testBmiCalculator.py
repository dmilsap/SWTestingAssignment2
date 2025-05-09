import pytest
from bmiCalculator import calculateBMI, outputBMICategory
# underweight
def testBMIUnderwightOFF():
    bmi = calculateBMI(108, 5, 5)
    assert bmi == 18.4
    assert outputBMICategory(bmi) == "Underweight"

# Normal
def testBMINormalOn1():
    bmi = calculateBMI(108.3, 5, 5)
    assert bmi == 18.5
    assert outputBMICategory(bmi) == "Normal weight"

def testBMINormalOn2():
    bmi = calculateBMI(146, 5, 5)
    assert bmi == 24.9
    assert outputBMICategory(bmi) == "Normal weight"

def testBMINormalOff2():
    bmi = calculateBMI(145.5, 5, 5)
    assert bmi == 24.8
    assert outputBMICategory(bmi) == "Normal weight"

#Overweight
def testBMIOverweightON1():
    bmi = calculateBMI(146.5, 5, 5)
    assert bmi == 25.0
    assert outputBMICategory(bmi) == "Overweight"
def testBMIOverweightOFF1():
    bmi = calculateBMI(147, 5, 5)
    assert bmi == 25.1
    assert outputBMICategory(bmi) == "Overweight"

def testBMIOverweightON2():
    bmi = calculateBMI(175.5, 5, 5)
    assert bmi == 29.9
    assert outputBMICategory(bmi) == "Overweight"
def testBMIOverweightOff2():
    bmi = calculateBMI(175, 5, 5)
    assert bmi == 29.8
    assert outputBMICategory(bmi) == "Overweight"


#Obese
def testBMIObeseON():
    bmi = calculateBMI(176, 5, 5)
    assert bmi == 30.0
    assert outputBMICategory(bmi) == "Obese"
def testBMIObeseOFF():
    bmi = calculateBMI(176.5, 5, 5)
    assert bmi == 30.1
    assert outputBMICategory(bmi) == "Obese"


#interior
def testBMIInterior():
    bmi = calculateBMI(120, 5, 5)
    assert bmi == 20.4
    assert outputBMICategory(bmi) == "Normal weight"







