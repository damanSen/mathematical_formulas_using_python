#Temperature degrees converter

#celsius to fahrenheit
def CelToFahr(celsius):
    return celsius*(9/5)+32

#fahrenheit to celsius
def FahrToCel(fahrenheit):
    return (fahrenheit-32)*(5/9)

# user input
print("Choose what to convert (only letter)")
choice = str(input("A. Celsius to Fahrenheit B. Fahrenheit to celsius : "))  

if choice.upper() == "A":
    celsius = int(input("Enter celsius: "))
    print(CelToFahr(celsius))

if choice.upper() == "B":
    fahrenheit = int(input("Enter fahrenheit: "))
    print(FahrToCel(fahrenheit))