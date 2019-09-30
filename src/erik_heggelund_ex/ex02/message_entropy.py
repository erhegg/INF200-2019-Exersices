from math import log as log2


def letter_freq(txt):
    txt = txt.lower()
    found_letters = {}
    for sign in txt:
        if sign in found_letters.keys():
            found_letters[sign] += 1
        else:
            found_letters[sign] = 1
    return found_letters


def entropy(message):
    letter_count = letter_freq(message)
    message_entropy = 0
    for sign in letter_count:
        occurances = letter_count[sign]
        frequency = occurances / len(message)
        message_entropy -= frequency * log2(frequency, 2)
    return message_entropy


if __name__ == "__main__":
    for msg in "", "aaaa", "aaba", "abcd", "This is a short text.":
        print("{:25}: {:8.3f} bits".format(msg, entropy(msg)))
