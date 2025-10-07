import sys


def main():
    """
    un programme qui transforme une string en Morse
    """
    morse_ch = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
    }
    # print(sys.argv)

    if len(sys.argv) != 2:
        print("AssertionError: the arguments are bad")
        return

    def is_valid(s): return all(ch.isalnum() or ch.isspace() for ch in s)
    if not is_valid(sys.argv[1]):
        print("AssertionError: the string contains invalid characters")
        return

    msg_morse = [morse_ch[elem.upper()]
                 for elem in sys.argv[1] if elem.upper() in morse_ch]
    print("".join(msg_morse))


main()
