# This program demonstrates the playfair cipher:

def remove_duplicates(w):
    seen = set()
    result = []
    for item in w:
        if item not in seen and item != ' ':
            result.append(item)
            seen.add(item)
    return result


def remove_spaces(w):
    result = []
    for item in w:
        if item != ' ':
            result.append(ord(item) - ord('a'))
    return result


message = "the key is hidden under the door pad"
word = "guidance"

# The following line calls remove_spaces function which will remove spaces and return message as index values.
message = remove_spaces(message)
# Construction of key: The key is table of size 5 * 5
key = [[-1 for _ in range(5)]for _ in range(5)]
index_set = set()
count = 0
word = remove_duplicates(word)

filler = 0
""" filler means the rest characters after the word """
word_length = len(word)
for i in range(5):
    for j in range(5):
        if count < word_length:
            index = ord(word[count]) - ord('a')
            key[i][j] = index
            index_set.add(index)
            count += 1
        else:
            while filler in index_set:
                filler += 1
            key[i][j] = filler
            index_set.add(filler)
            # for using only one out of i or j.
            if filler == 8:
                filler = 10

# Finding the digrams in the message:
digrams = [[-1 for _ in range(2)] for _ in range(len(message))]
if len(message) % 2 != 0:
    message.append(-1)
# -1 denotes that there is nothing there.
num_digram = 0
# num_digram denotes the digram being filled.
i = 0
while i < len(message) - 1:
    first = message[i]
    second = message[i + 1]
    if first == second:
        second = ord('x') - ord('a')
        i += 1
    else:
        i += 2
    digrams[num_digram][0] = first
    digrams[num_digram][1] = second
    num_digram += 1

# Encrypting:

def find_pos(char, key):
    for i in range(5):
        for j in range(5):
            if key[i][j] == char:
                return i, j
    return -1, -1


playfair_encryption = ""
for i in range(num_digram):
    first_row, first_col = find_pos(digrams[i][0], key)
    second_row, second_col = find_pos(digrams[i][1], key)

    if first_row == second_row:
        first_index = key[first_row][(first_col + 1) % 5]
        second_index = key[first_row][(second_col + 1) % 5]
    elif first_col == second_col:
        first_index = key[(first_row + 1) % 5][first_col]
        second_index = key[(second_row + 1) % 5][first_col]
    else:
        first_index = key[first_row][second_col]
        second_index = key[second_row][first_col]
    playfair_encryption += chr(ord('a') + first_index)
    playfair_encryption += chr(ord('a') + second_index)
print("The playfair encryption gives:")
print(playfair_encryption)

# Decryption:

playfair_decryption = ""

# Loop increment adjusted to process two characters at a time properly
for i in range(0, len(playfair_encryption) - 1, 2):
    first = ord(playfair_encryption[i]) - ord('a')
    second = ord(playfair_encryption[i + 1]) - ord('a')
    first_row, first_col = find_pos(first, key)
    second_row, second_col = find_pos(second, key)

    if first_row == second_row:
        # Decrement the column index and wrap around using modulo 5
        first_index = key[first_row][(first_col - 1) % 5]
        second_index = key[first_row][(second_col - 1) % 5]
    elif first_col == second_col:
        # Decrement the row index and wrap around using modulo 5
        first_index = key[(first_row - 1) % 5][first_col]
        second_index = key[(second_row - 1) % 5][first_col]
    else:
        # Swap columns for rectangle rule
        first_index = key[first_row][second_col]
        second_index = key[second_row][first_col]

    playfair_decryption += chr(ord('a') + first_index)
    playfair_decryption += chr(ord('a') + second_index)

print("On decryption, we get:")
print(playfair_decryption)