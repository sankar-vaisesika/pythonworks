def split_and_join(line):
    words=line.split()
    return "-".join(words)
print(split_and_join("this is a line"))