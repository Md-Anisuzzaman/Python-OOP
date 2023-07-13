def do_something(work):
    print("Do something inside")

    def inner(*args, **kwargs):
        print("Enter inner")
        work(*args, **kwargs)
    return inner

@do_something
def calculation(n1, n2):
    result = n1 * n2
    print(result)

calculation(5,5)
