from calculator import AdvancedCalculator
from helper import validate_number, validate_operation

def display_menu():
    """Display the calculator menu."""
    print("\n=== Scientific Calculator ===")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Square Root (√)")
    print("6. Power (^)")
    print("7. Natural Logarithm (ln)")
    print("8. Sine (sin)")
    print("9. Cosine (cos)")
    print("10. Tangent (tan)")
    print("11. View History")
    print("12. Exit")
    print("========================")

def main():
    """Main program loop."""
    calc = AdvancedCalculator()
    
    while True:
        try:
            display_menu()
            choice = input("Enter your choice (1-12): ").strip()
            
            if choice == '12':
                print("Thank you for using the Scientific Calculator!")
                break
                
            if choice == '11':
                history = calc.view_history()
                print("\n=== Calculation History ===")
                print(history)
                continue
            
            # Validate operation choice
            if not choice.isdigit() or int(choice) < 1 or int(choice) > 12:
                print("Invalid choice. Please enter a number between 1 and 12.")
                continue
            
            # Input handling for different operations
            if choice in ['1', '2', '3', '4', '6']:  # Two-number operations
                valid, x, error = validate_number(input("Enter first number: "))
                if not valid:
                    print(error)
                    continue
                    
                valid, y, error = validate_number(input("Enter second number: "))
                if not valid:
                    print(error)
                    continue
                
                if choice == '1':
                    result = calc.add(x, y)
                elif choice == '2':
                    result = calc.subtract(x, y)
                elif choice == '3':
                    result = calc.multiply(x, y)
                elif choice == '4':
                    result = calc.divide(x, y)
                else:  # Power
                    result = calc.power(x, y)
                    
            elif choice in ['8', '9', '10']:  # Trigonometric functions
                valid, degrees, error = validate_number(input("Enter angle in degrees: "))
                if not valid:
                    print(error)
                    continue
                
                # Convert degrees to radians
                radians = calc.degrees_to_radians(degrees)
                
                if choice == '8':
                    result = calc.sin(radians)
                elif choice == '9':
                    result = calc.cos(radians)
                else:
                    result = calc.tan(radians)
                    
            else:  # Single-number operations (sqrt, ln)
                valid, x, error = validate_number(input("Enter number: "))
                if not valid:
                    print(error)
                    continue
                
                if choice == '5':
                    result = calc.square_root(x)
                else:  # Natural logarithm
                    result = calc.logarithm(x)
            
            print(f"Result: {result}")
            
        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()