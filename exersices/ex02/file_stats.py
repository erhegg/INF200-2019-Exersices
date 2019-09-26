def char_counts(textfilename):
    file_string = open(textfilename).read()
    result = [0 for _ in range(256)]
    for symbol in file_string:
        result[ord(symbol)] += 1
    return result


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
