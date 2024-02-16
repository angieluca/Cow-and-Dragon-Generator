import sys
from heifer_generator import HeiferGenerator
from cow import Cow
from dragon import Dragon
from ice_dragon import IceDragon


def list_cows(cows):
    cow_list = []
    for cow in cows:  # iterates through Python list of cow objects
        cow_list.append(Cow.get_name(cow))  # calls get_name() to get the name and not just the memory address
    return " ".join(cow_list)  # returns the available cows as a string list


def find_cow(name, cows):
    cow_exists = None
    if name in cows:
        cow_exists = name  # returns the name if the name exists in the Python list of cow objects
    return cow_exists


if __name__ == '__main__':

    cows = HeiferGenerator.get_cows()  # Python list of cow objects

    # first checks that arguments other than the file name were passed
    if len(sys.argv) > 1:

        # Lists the available cows
        if sys.argv[1] == '-l':
            print("Cows available:", list_cows(cows))

        # Prints out the MESSAGE using the specified COW
        elif sys.argv[1] == '-n':
            name = sys.argv[2]
            if find_cow(name, list_cows(cows)) is not None:  # checks if cow name exists in the string list of names
                output_msg = " ".join(sys.argv[3:])  # turn message list into a string
                print(output_msg)
                for i in range(len(cows)):  # iterate through available cows
                    if name == Cow.get_name(cows[i]):
                        print(Cow.get_image(cows[i]))
                if name == 'dragon':
                    print("This dragon can breathe fire.")
                elif name == 'ice-dragon':
                    print("This dragon cannot breathe fire.")
            else:  # cow name does not exist
                print("Could not find", name, "cow!")

        # Prints out the MESSAGE using the default COW
        else:
            output_msg = " ".join(sys.argv[1:])  # turn message list into a string
            print(output_msg)
            print(Cow.get_image(cows[0]))

    # prints default cow without any message
    else:
        print(Cow.get_image(cows[0]))



