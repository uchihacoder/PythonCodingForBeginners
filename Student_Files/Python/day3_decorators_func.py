# since we are using *args and **kwargs, we can decorate functions with different signatures
import datetime
import time


def capture_timing_decorator(function):
    def on_call(*args, **kwargs):
        start = time.perf_counter()
        rc = function(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"Elapsed time: {elapsed}")

        return rc
    return on_call


def log_stuff(function, message):
    with open("kevin_log.txt", "a+") as file:
        file.write(
            f"{message} -- {function.__name__} called at {str(datetime.datetime.today())}\n")


def my_decorator(function):
    def on_call(*args, **kwargs):
        log_stuff(function, "my_decorator: before")
        rc = function(*args, **kwargs)
        log_stuff(function, "my_decorator: after")

        return rc
    return on_call


@capture_timing_decorator
@my_decorator
def my_function(x, y):
    print(f"x: {x}, y: {y}")


@capture_timing_decorator
@my_decorator
def another_function(x):
    print(f"x: {x}")


my_function(1, 2)

another_function(4)
