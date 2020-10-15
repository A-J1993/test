def calc(op, a ,b):
    if str(op) in ("+", "-", "x","/", "^"):
        if str(op) == "+":
            return int(a) + int(b)
        elif str(op) == "-":
            return int(a) - int(b)
        elif str(op) == "x":
            return int(a) * int(b)
        elif:
            return float(a) / float(b)
        else:
            return int(a)^int(b)
    else:
        print("Have not inputted a valid operation")

def split_text(text_file):
    def read_in(text_file):
        with open(text_file, 'r') as f:
            text_string = f.read()
        return text_string
    text_string = read_in(text_file)
    text_string_list = text_string.split('\n')
    running_total = 0
    for line in text_string_list:
        split_line = line.split(' ')
        result = calc(split_line[1], split_line[2], split_line[3])
        running_total += result
    return running_total

print(split_text("text.txt"))