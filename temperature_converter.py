#!/usr/local/bin/python3

import colored

# decoration
print(colored.stylize("\n---- | Convert temperature degrees | ----\n", colored.fg("red")))

# user interaction
print("From which temperature degree do you want to convert?")
fromT = input("'c' for Celsius\n'f' for Fahrenheit\n'k' for Kelvin\n: ")
temperature = float(input("\nTemperature: "))
print("\nTo which temperature degree do you want to convert?")
toT = input("'c' for Celsius\n'f' for Fahrenheit\n'k' for Kelvin\n: ")
print()

# functions
def celsiusToFahrenheit(temperature):
    return temperature*9/5+32

def celsiusToKelvin(temperature):
    return temperature+273.15

def fahrenheitToCelsius(temperature):
    return (temperature-32)*5/9

def kelvinToCelsius(temperature):
    return temperature-273.15

# main program
if fromT == toT:
    print(f"No conversion needed.\nTemperature: {temperature} °C / °F / K")

elif fromT == "c" and toT == "f":
    print(f"Conversion from Celsius to Fahrenheit.\nTemperature in °C: {temperature}\nTemperature in °F: {round(celsiusToFahrenheit(temperature), 3)}\n")
elif fromT == "c" and toT == "k":
    print(f"Conversion from Celsius to Kelvin.\nTemperature in °C: {temperature}\nTemperature in K: {round(celsiusToKelvin(temperature), 3)}\n")

elif fromT == "f" and toT == "c":
    print(f"Conversion from Fahrenheit to Celsius.\nTemperature in °F: {temperature}\nTemperature in °C: {round(fahrenheitToCelsius(temperature), 3)}\n")
elif fromT == "f" and toT == "k":
    print(f"Conversion from Fahrenheit to Kelvin.\nTemperature in °F: {temperature}\nTemperature in K: {round(celsiusToKelvin(fahrenheitToCelsius(temperature)), 3)}\n")

elif fromT == "k" and toT == "c":
    print(f"Conversion from Kelvin to Celsius.\nTemperature in K: {temperature}\nTemperature in °C: {round(kelvinToCelsius(temperature), 3)}\n")
elif fromT == "k" and toT == "f":
    print(f"Conversion from Kelvin to Fahrenheit.\nTemperature in K: {temperature}\nTemperature in °F: {round(celsiusToFahrenheit(kelvinToCelsius(temperature)), 3)}\n")
