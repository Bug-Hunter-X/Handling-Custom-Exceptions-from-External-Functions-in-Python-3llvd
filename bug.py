def function_with_uncommon_error(x):
    if x == 0:
        return 1 / x  # ZeroDivisionError, but not the uncommon part

    try:
        result = some_external_function(x)  # Assume this function might raise a custom exception
        return result
    except SomeCustomException as e:
        # This is where the uncommon part comes in
        print(f"Encountered an uncommon exception: {e}")
        return None
    except Exception as e:
        print(f"Caught an unexpected error: {e}")
        return None

class SomeCustomException(Exception):
    pass

def some_external_function(x):
    # Simulates some external function that might raise a custom exception
    if x > 10:
        raise SomeCustomException("x is too large!")
    return x * 2