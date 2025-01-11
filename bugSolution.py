def function_with_uncommon_error(x):
    if x == 0:
        return None # Handle ZeroDivisionError explicitly

    try:
        result = some_external_function(x)
        return result
    except SomeCustomException as e:
        print(f"Encountered an uncommon exception: {e}")
        # Perform alternative actions or logging
        return None
    except Exception as e:
        print(f"Caught an unexpected error: {type(e).__name__}: {e}")
        # Consider more sophisticated logging or error reporting
        return None

class SomeCustomException(Exception):
    pass

def some_external_function(x):
    if x > 10:
        raise SomeCustomException("x is too large!")
    return x * 2