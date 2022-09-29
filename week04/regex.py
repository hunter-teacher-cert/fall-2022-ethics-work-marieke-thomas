import re


def find_name(line):
    # Two or Three word names (meaning a capital letter followed by lower case letters)
    pattern = r"([A-Z][a-z]+ [A-Z][a-z]+(?: [A-Z][a-z]+)?)"
    result = re.findall(pattern, line)

    # Names of the format Ms. Thomas
    pattern = r'(?:Mrs\.|Mr\.|Dr\.|Miss|Ms\.) [A-Z][a-z]+'
    result = result + re.findall(pattern, line)

    #Names with single letters such as Dr. S. Howard, J.K. Rowling, etc
    pattern = r'(Dr\. [A-Z]\. [A-Z][a-z]+|[A-Z]\. ?[A-Z]\. [A-Z][a-z]+|[A-Z][a-z]+ [A-Z]\. [A-Z][a-z]+|[A-Z]\. [A-Z][a-z]+)'
    result = result + re.findall(pattern, line)

    return result

# I chose not to have the program recognize names that are oddly-formatted (such as "marieke thomas") because I don't want it to print pretty much every word it finds.

f = open("names.txt")
for line in f.readlines():
    # print(line)
    result = find_name(line)
    if (len(result) > 0):
        print(result)
