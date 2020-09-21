decoding_map = {str(x + 1): chr(x + ord('A')) for x in range(26)}


def decode(msg):
    accumulated = []

    for i, letter in enumerate(msg):
        if i == 0:
            accumulated.append(decoding_map[letter])
        else:
            new_ones = []

            for item in accumulated:
                if msg[i - 1] != '0' and \
                        0 < int(msg[i - 1] + letter) < 27 and \
                        item[-1] == decoding_map[msg[i - 1]]:
                    new_ones.append(item[:-1] + decoding_map[msg[i - 1] + letter])
                if letter != '0':
                    new_ones.append(item + decoding_map[letter])

            accumulated = new_ones

    return len(accumulated)


encoded_msg = "210213"

print(encoded_msg)
print(decode(encoded_msg))
