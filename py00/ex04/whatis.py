import sys

def is_even(n: int):
    if n % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

def main():
    if len(sys.argv) == 1:
        return
    try:
        assert len(sys.argv) == 2, "Exactly one argument must be provided"
        try:
            arg = int(sys.argv[1])
        except ValueError:
            raise AssertionError("The argument is not an integer")
    except AssertionError as e:
        print("AssertionError:", e)
        return
    is_even(arg)

if __name__ == "__main__":
    main()
