symbols = {"-", ",", ".", "!", "?"}
count_lines = 0

with open("text.txt", "r") as file:
    for line in file:
        if count_lines % 2 == 0:
            for symbol in symbols:
                line = line.replace(symbol, "@")

            reversed_line_string = " ".join(line.split()[::-1])
            print(reversed_line_string, end="\n")

        count_lines += 1