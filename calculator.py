from operations import Addition, Multiplication, Division

class Calculator:
    def __init__(self):
        self.operations = {
            "add": Addition(),
            "multiply": Multiplication(),
            "divide": Division(),
        }

    def calculate(self, operation, a, b):
        if operation not in self.operations:
            raise ValueError(f"Unsupported operation: {operation}")
        return self.operations[operation].execute(a, b)