def validate_number(value):
    """
    Validate if the input string can be converted to a float number.
    
    Args:
        value (str): The input string to validate
        
    Returns:
        tuple: (bool, float or None, str) - (is_valid, converted_value, error_message)
    """
    try:
        num = float(value)
        return True, num, ""
    except ValueError:
        return False, None, "Invalid input: Please enter a valid number."
    except Exception as e:
        return False, None, f"Unexpected error: {str(e)}"

def validate_operation(operation, valid_operations):
    """
    Validate if the operation is in the list of valid operations.
    
    Args:
        operation (str): The operation to validate
        valid_operations (list): List of valid operations
        
    Returns:
        tuple: (bool, str) - (is_valid, error_message)
    """
    if operation.lower() in valid_operations:
        return True, ""
    return False, f"Invalid operation. Valid operations are: {', '.join(valid_operations)}"