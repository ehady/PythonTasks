class FileHandler(object):
    def __init__(self, filename, flag):
        self.file = filename
        self.flag = flag

    def __enter__(self):
        try:
            self.resource = open(self.file, self.flag)
        except FileNotFoundError:
            print(f"Warning: {self.file} not found. Creating a new file.")
            self.resource = open(self.file, "w")
        return self.resource
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is OSError:
            print(f"Error occurred: {exc_val}")
            return True
        self.resource.close()


with FileHandler("any_file.txt", "w") as file:
    file.write("something")

with FileHandler("any_file_name.txt", "r") as file:
    file.readline()
