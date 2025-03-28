class Operation:
    def execute(self, a, b):
        raise NotImplementedError("This method should be overridden in subclasses.")


class Addition(Operation):
    def execute(self, a, b):
        return a + b


class Multiplication(Operation):
    def execute(self, a, b):
        return a * b


class Division(Operation):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b