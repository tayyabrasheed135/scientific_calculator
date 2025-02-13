import math
from datetime import datetime
from helper import validate_number, validate_operation

class ScientificCalculator:
    """Base calculator class with basic and scientific operations."""
    
    def __init__(self):
        """Initialize the calculator with a history file."""
        self.history_file = "history.txt"
        
    def add(self, x, y):
        """Add two numbers."""
        result = x + y
        self._log_operation(f"{x} + {y} = {result}")
        return result
    
    def subtract(self, x, y):
        """Subtract two numbers."""
        result = x - y
        self._log_operation(f"{x} - {y} = {result}")
        return result
    
    def multiply(self, x, y):
        """Multiply two numbers."""
        result = x * y
        self._log_operation(f"{x} * {y} = {result}")
        return result
    
    def divide(self, x, y):
        """Divide two numbers."""
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        result = x / y
        self._log_operation(f"{x} / {y} = {result}")
        return result
    
    def square_root(self, x):
        """Calculate square root of a number."""
        if x < 0:
            raise ValueError("Cannot calculate square root of a negative number")
        result = math.sqrt(x)
        self._log_operation(f"√{x} = {result}")
        return result
    
    def power(self, x, y):
        """Calculate x raised to power y."""
        result = math.pow(x, y)
        self._log_operation(f"{x}^{y} = {result}")
        return result
    
    def logarithm(self, x):
        """Calculate natural logarithm of a number."""
        if x <= 0:
            raise ValueError("Cannot calculate logarithm of non-positive number")
        result = math.log(x)
        self._log_operation(f"ln({x}) = {result}")
        return result
    
    def _log_operation(self, operation_str):
        """Log operation to history file."""
        try:
            with open(self.history_file, 'a') as f:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{timestamp}] {operation_str}\n")
        except Exception as e:
            print(f"Warning: Could not log operation to history file: {str(e)}")
    
    def view_history(self):
        """View calculation history."""
        try:
            with open(self.history_file, 'r') as f:
                history = f.read()
                if not history:
                    return "No calculation history found."
                return history
        except FileNotFoundError:
            return "No history file found."
        except Exception as e:
            return f"Error reading history file: {str(e)}"


class AdvancedCalculator(ScientificCalculator):
    """Advanced calculator with trigonometric functions."""
    
    def sin(self, x):
        """Calculate sine of an angle (in radians)."""
        result = math.sin(x)
        self._log_operation(f"sin({x}) = {result}")
        return result
    
    def cos(self, x):
        """Calculate cosine of an angle (in radians)."""
        result = math.cos(x)
        self._log_operation(f"cos({x}) = {result}")
        return result
    
    def tan(self, x):
        """Calculate tangent of an angle (in radians)."""
        result = math.tan(x)
        self._log_operation(f"tan({x}) = {result}")
        return result
    
    def degrees_to_radians(self, degrees):
        """Convert degrees to radians."""
        return math.radians(degrees)