from contextlib import contextmanager


@contextmanager
def file_handler(filename, flag):
    resource = None
    try:
        resource = open(filename, flag)
        yield resource
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Creating a new file.")
        resource = open(filename, "w")
        yield resource
    finally:
        if resource:
            resource.close()

with file_handler("any_file.txt", "w") as file:
   file.write("something")

with file_handler("any_file_name", "r") as file:
    file.readline()