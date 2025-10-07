import sys
import string


def main():
    """
  This script analyzes a single string passed as a command-line
  argument and counts different types of characters in it.

  Usage:
      python3 building.py "Your string here"

  The script counts and displays the following:
      - Number of uppercase letters
      - Number of lowercase letters
      - Number of punctuation marks
      - Number of spaces
      - Number of digits

  Constraints:
      - If no argument is provided, it displays a usage message.
      - If more than one argument is provided, it raises an assertion error.

  Example:
      python3 building.py "Hello, World! 123"

      Output:
      2 upper letters
      8 lower letters
      2 punctuation marks
      2 spaces
      3 digits
  """

    if len(sys.argv) == 1:
        str = input("What is the text to count?\n")
    elif len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
        return
    else:
        str = sys.argv[1]

    UpperCases = 0
    LowerCases = 0
    PunctuationCases = 0
    Spaces = 0
    Digits = 0

    for char in str:
        if char.isupper():
            UpperCases += 1
        elif char.islower():
            LowerCases += 1
        elif char in string.punctuation:
            PunctuationCases += 1
        elif char.isdigit():
            Digits += 1
        elif char.isspace():
            Spaces += 1

    total = UpperCases + LowerCases + PunctuationCases + Digits + Spaces

    print(f"The text contains {total} characters:")
    print(f"{UpperCases} upper letters")
    print(f"{LowerCases} lower letters")
    print(f"{PunctuationCases} punctuation marks")
    print(f"{Spaces} spaces")
    print(f"{Digits} digits")


if __name__ == "__main__":
    main()
# print(main.__doc__)
