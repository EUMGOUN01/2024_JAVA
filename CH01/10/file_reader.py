from pathlib import Path

path = Path('CH01\\10\\pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()

# filename = 'CH01\\10\\pi_digits.txt'

# with open(filename) as file_object:
#     lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())