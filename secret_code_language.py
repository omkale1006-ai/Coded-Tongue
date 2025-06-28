# writ a python program to translate a message into secret code languag. use the rules below to translate normal english into secret code language
# coding: 
# if the word contains atleast 3 characters, remove the first letter and append it at the end 
# now append three characters at the the starting and the end
# else:
# simply reverse the string 

# decoding:
# if the word contains less than 3 characters, reverse it
# else:
# remove 3 random characters from start and end now remove the last letter and append it to the beginning


def secret_code():
    user_input = input("Enter your message to convert: ")
    words = user_input.split(" ")

    coding = input("Give 1 for coding and 2 for decoding: ")

    if coding == "1":
        # Encoding
        new_words = []
        for word in words:
            if len(word) >= 3:
                r1 = "dfg"
                r2 = "hty"
                code_word = r1 + word[1:] + word[0] + r2
                new_words.append(code_word)
            else:
                new_words.append(word[::-1])
        print("Coded message:", " ".join(new_words))

    elif coding == "2":
        password=input("Enter your password to access the decode language:")
        pas= "Omkale@1006" 
        if password==pas:
        # Decoding
            new_words = []
            for word in words:
                if len(word) >= 3:
                    core_word = word[3:-3]  # Remove the 3 letters from both ends
                    decoded_word = core_word[-1] + core_word[:-1]  # Last letter to front
                    new_words.append(decoded_word)
                else:
                    new_words.append(word[::-1])
            print("Decoded message:", " ".join(new_words))
        else:
            print("Pssword incorrect plasece inter correct password")

    else:
        print("Invalid input. Please choose 1 or 2.")

# Run the function
secret_code()
