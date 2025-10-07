##########
# PART 2 #
##########
import sys


def main():
    """
    Un programme qui prend en parametre une str et un int et qui
    retourne les mots de la str
    qui sont plus long que le int passé en paramètre
    """
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return

    def is_valid_str(s): return all(ch.isalpha() or ch.isspace() for ch in s)
    if not is_valid_str(sys.argv[1]):
        print("AssertionError: the string contains invalid characters")
        return

    try:
        num = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    words = sys.argv[1].split(" ")

    newList = [elem for elem in words if len(elem) > num]
    print(newList)


if __name__ == "__main__":
    main()
