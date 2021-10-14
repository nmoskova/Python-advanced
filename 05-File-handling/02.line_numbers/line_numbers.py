import string

punctuation_marks = string.punctuation
count_lines = 1

with open("text.txt", "r") as reading_file, open("output.txt", "w") as output_text:
    for line in reading_file:
        count_symbols = 0
        count_letters = 0
        for ch in line:
            if ch.isalpha():
                count_letters += 1
            elif ch in punctuation_marks:
                count_symbols += 1
        output_text.write(f"Line {count_lines}: {line.strip()} ({count_letters})({count_symbols})\n")

        count_lines += 1