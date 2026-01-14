# cube.py

def find_cube(num):
    """Return cube of a number."""
    return num * num * num


if __name__ == "__main__":
    num = float(input("Enter a number: "))
    cube = find_cube(num)
    print("Cube of the number is:", cube)