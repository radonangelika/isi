char_input = input("Podaj znak: ")
first_char = char_input[0]

# Sposób 1
if first_char.isdigit():
    print("To jest cyfra. (isdigit)")

# Sposób 2
if isinstance(first_char, str) and '0' <= first_char <= '9':
    print("To jest cyfra. (isinstance)")
else:
    print("To NIE jest cyfra.")