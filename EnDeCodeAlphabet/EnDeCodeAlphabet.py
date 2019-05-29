from __future__ import print_function, division


def encodeAlph(string):
    saved = string[0]
    counter = 0
    result = ''
    for char in string:
        if(char == saved):
            counter += 1
        else:
            result = result + str(counter) + saved
            saved = char
            counter = 1
    result = result + str(counter) + string[-1]
    return result


def decodeAlph(string):
    result = ''
    for i in range(0, len(string), 2):
        result = result + string[i+1]*int(string[i])
    return result


if __name__ == "__main__":
    assert '4A3B2C1D2A' == encodeAlph('AAAABBBCCDAA')
    assert 'AAAABBBCCDAA' == decodeAlph('4A3B2C1D2A')
