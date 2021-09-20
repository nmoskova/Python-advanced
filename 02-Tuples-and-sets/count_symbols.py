text = input()
characters = {}

for ch in text:
    if ch not in characters:
        characters[ch] = 0

    characters[ch] += 1

[print(f"{key}: {value} time/s") for key, value in sorted(characters.items())]
