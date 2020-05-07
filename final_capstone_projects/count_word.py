# count number of words in string

def word_counter():
    string = input("Give me a sentence to work with: ").lower()

    string_count = string.count(" ") +1
    print("Nr. of words in this sentence: ", string_count)


    # word = string.split(" ")

    # word_count = 0

    # for word in string:
    #     print("hi")


word_counter()