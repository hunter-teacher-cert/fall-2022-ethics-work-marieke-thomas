import re


def find_name(line):
    pattern = r"[A-Z][a-z]+ [A-Z][a-z]+"
    # pattern = r"([A-Z][a-z]+ ){1,2}[A-Z][a-z]+"
    # pattern = r'(a(?:bc)?d)'
    result = re.findall(pattern, line)

    pattern = r'(?:Mrs\.|Mr\.|Dr\.|Miss|Ms\.) [A-Z][a-z]+'
    result = result + re.findall(pattern, line)

    pattern = r'(Dr\. [A-Z]\. [A-Z][a-z]+|[A-Z]\. [A-Z]\. [A-Z][a-z]+|[A-Z]\. [A-Z][a-z]+)'
    result = result + re.findall(pattern, line)

    # pattern = r"[A-Z][a-z]+ [A-Z][a-z]+ [A-Z][a-z]+"
    # result = result + re.findall(pattern,line)

    return result


f = open("names.txt")
for line in f.readlines():
    # print(line)
    result = find_name(line)
    if (len(result) > 0):
        print(result)

# import re
# def find_date(line):
#     pattern = r"\d{1,2}/\d{1,2}/\d{2,4}"
#     result = re.findall(pattern,line)

#     pattern=r'(October|Oct|November|Nov)( [0-9]{1,2}, [0-9]{4})'
#     result = result + re.findall(pattern,line)
#     return result

# f = open("names.txt")
# for line in f.readlines():
#     #print(line)
#     result = find_date(line)
#     if (len(result)>0):
#         print(result)
