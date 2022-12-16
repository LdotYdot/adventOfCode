import os

# gets file relative to input directory (e.g. pass in "day1/input.txt")
def read_file(filepath):
    with open(os.getcwd() + "\\inputs\\" + filepath, "r") as file:
        return file.read()