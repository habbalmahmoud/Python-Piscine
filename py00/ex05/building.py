import sys

def main(str, flagg):
    """The main function"""
    char = 0
    upper = 0
    lower = 0
    punc = 0
    space = 0
    num = 0
    flag = 0

    for ser in str:
        if flag == 0 and flagg == 0:
            flag += 1
            continue
        for s in ser:
            if 'a' <= s <= 'z':
                lower += 1
            elif 'A' <= s <= 'Z':
                upper += 1
            elif '!' <= s <= '/':
                punc += 1
            elif '\t' <= s <= '\r' and s == ' ':
                space += 1
            elif '0' <= s <= '9':
                num += 1
            char += 1

    print("The text contains", char, "characters")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punc, "punctuation marks")
    print(space, "spaces")
    print(num, "digits")


if __name__ == "__main__":

    argc = 0
    flag = 0
    for arg in sys.argv:
        argc += 1
    if argc > 2:
        print("AssertionError: more than one argument is provided")
        sys.exit(1)
    if argc == 2:
        args = sys.argv
    else:
        print("Enter Something!")
        args = sys.stdin.readlines()
        flag = 1
    main(args, flag)
