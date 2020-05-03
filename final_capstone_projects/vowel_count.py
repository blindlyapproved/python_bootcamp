# Count number of vowels in string

def vowel_count():

    count_a = 0
    count_e = 0
    count_i = 0
    count_o = 0
    count_u = 0

    string = input("Let me count the vowels for your string. Insert your string here: ")

    for char in string:
        if char in "a":
            count_a = count_a + 1
        if char in "u":
            count_u = count_u + 1
        if char in "o":
            count_o = count_o + 1
        if char in "d":
            count_e = count_e + 1
        if char in "i":
            count_i = count_i + 1


    print(f"Total times letter A found: {count_a}")
    print(f"Total times letter U found: {count_u}")
    print(f"Total times letter O found: {count_o}")
    print(f"Total times letter E found: {count_e}")
    print(f"Total times letter I found: {count_i}")

vowel_count()