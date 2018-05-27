filename = 'pi_string.py'
read_line = []

with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)
    for line in lines:
        line = line.replace('else', 'fourxxxx')
        read_line.append(line)
        print(line)

print(read_line)

