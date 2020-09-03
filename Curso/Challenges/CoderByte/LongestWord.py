import string


def LongestWord(sen):
    longest = ""
    for c in string.punctuation:
        sen = sen.replace(c, "")
    sen = sen.split()
    for word in sen:
        if len(word) > len(longest):
            longest = word
    sen = longest
    return sen


# Main
print(LongestWord(input()))
