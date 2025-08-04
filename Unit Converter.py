def length_menu():
    m = float(input("Enter length in meters: "))
    print(f"{m} m = {m*100:.2f} cm")

def weight_menu():
    kg = float(input("Enter weight in kilograms: "))
    print(f"{kg} kg = {kg*1000:.2f} g")

def temp_menu():
    c = float(input("Enter temperature in °C: "))
    f = (c * 9/5) + 32
    print(f"{c} °C = {f:.2f} °F")

while True:
    print("\nUnit Converter")
    print("1) Length  2) Weight  3) Temperature  4) Exit")
    choice = input("Select option: ")
    if choice == '1':
        length_menu()
    elif choice == '2':
        weight_menu()
    elif choice == '3':
        temp_menu()
    elif choice == '4':
        print("done")
        break
    else:
        print("Invalid choice, try again.")