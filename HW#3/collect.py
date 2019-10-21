import os
import re
import sys


def aggregate(gender):
    if gender not in ['male', 'female']:
        raise NameError(
            "No matching files found for the requested argument!")
    try:
        os.remove(f'{gender}Results.txt')
    except FileNotFoundError as e:
        pass

    fW = open(f'{gender}Results.txt', "a+")

    for i in os.listdir(os.path.join(os.getcwd(), "data")):
        if gender == "female":
            if not i.startswith(".") and re.search(r'.*(she|her\s|female).*', i, re.IGNORECASE):
                with open(os.path.join(os.getcwd(), "data", i)) as fR:
                    fW.write(f'filename: {i}\n')
                    for line in fR:
                        fW.write(line)
        elif gender == "male":
            if not i.startswith(".") and not re.search(r'.*(she|her\s|female).*', i, re.IGNORECASE):
                with open(os.path.join(os.getcwd(), "data", i)) as fR:
                    fW.write(f'filename: {i}\n')
                    for line in fR:
                        fW.write(line)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise NameError("Please enter gender!")
    aggregate(sys.argv[1])
