program_is_on = True
while program_is_on:
    user_input = input("Enter a string:")
    if user_input == "":
        print("Enter a non-empty string")
    else:
        vowels_count = 0
        vowels = ["A", "a", "i", "I", "o", "O", "u", "U", "e", "E"]
        for letter in user_input:
            if letter in vowels:
                vowels_count += 1
        print("The Number of Vowels in", user_input, "is", vowels_count)
        program_is_on = False