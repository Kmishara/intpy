class Calculator:
    def __init__(self,a:float,b:float,operation:str):
        self.a = a
        self.b = b
        self.operation = operation.lower()
    def calculate(self):
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.operation == "multiply":
            return self.a * self.b
        elif self.operation == "division":
            if self.b != 0:
               return self.a / self.b 
            else:
                return "Division by zero"
        else:
            return "Invalid operation"
a = float(input("enter a first number:"))
b = float(input("enter a second number:"))
operation = input("enter a operation (add,subtract,multiply,division):")
cal = Calculator(a,b,operation)
result = cal.calculate()
print("Result:",result)