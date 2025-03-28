from calculator import Calculator
from logger import setup_logger

def main():
    logger = setup_logger()
    calc = Calculator()

    try:
        a = complex(input("Enter the first complex number (e.g., 1+2j): "))
        b = complex(input("Enter the second complex number (e.g., 3+4j): "))
        operation = input("Enter operation (add, multiply, divide): ").strip()

        result = calc.calculate(operation, a, b)
        logger.info(f"Operation: {operation}, Inputs: {a}, {b}, Result: {result}")
        print(f"Result: {result}")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        print(f"Error: {e}")

if __name__ == "__main__":
    main()