
def valid_skyphrases_number():

    file = 'skychallenge_skyphrase_input.txt'
    valid = 0
    with open(file, 'r') as f:
        line = f.readline()
        while line:
            split_line = line.split()
            len_split_line = len(split_line)
            for i, word in enumerate(split_line):
                if split_line.count(word) > 1:
                    break
            else:
                if i == len_split_line - 1:
                    valid += 1
            line = f.readline()
    return valid


if __name__ == '__main__':
    print(f"Valid skyphrases number:{valid_skyphrases_number()}")
else:
	print('Run this script directly')