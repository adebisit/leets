import time

def timeHandlerWrapper(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function runtime -> {end - start}")
        return result
    return wrapper
