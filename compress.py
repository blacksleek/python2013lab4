def compress():
    import re
    infile = open("gutenberg.txt", mode = "r")
    compressed_file = open("compressed_file.txt", mode = "a")

    word_list = []
    length = 0
    for line in infile.readlines():
        for element in re.findall(r"[\w']+|[!@#$%^&*(){}_+-=:';,./?>< ]", line):
            if len(element) < 5:
                word_list.append(element)
            else:
                pass
            
    for line in infile.readlines():
        for element in re.findall(r"[\w']+|[!@#$%^&*(){}_+-=:';,./?>< ]", line):
            if element in word_list:
                compressed_file.write(str(word_list.index(element)) + ".")
            else:
                word_list.append(element)
                compressed_file.write(str(word_list.index(element)) + ".")
        compressed_file.write("\n")

    compressed_file.write("\n")
    for i in word_list:
        compressed_file.write(i + ".")

    infile.close()
    compressed_file.close()

compress()
