from re import split


def sum_of_all_numbers():
    file_name = 'test_data.txt'

    with open(file_name, 'r') as file_with_data:
        file_content = file_with_data.read()

    split_file_content = split(r'[^-0-9]', file_content)

    while '' in split_file_content:
        split_file_content.remove('')

    split_file_content = map(int, split_file_content)
    return sum(split_file_content)


if __name__ == '__main__':
    print(f"Sum of all numbers in file: {sum_of_all_numbers()}")
else:
    print("Run this script directly")
