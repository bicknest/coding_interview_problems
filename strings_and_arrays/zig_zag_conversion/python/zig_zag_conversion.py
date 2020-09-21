# Traverse the string using rules of zig zagging and append the character onto corresponding
# character arrays

def convert(message, num_rows):
    char_lists = []
    for num in range(num_rows):
        char_lists.append([])

    going_down = True
    row_index = 0

    if num_rows == 1:
        return message

    for char in message:
        char_lists[row_index].append(char)
        if row_index == (num_rows - 1) and going_down is True:
            going_down = False
        if row_index == 0 and going_down is False:
            going_down = True
        if going_down is True:
            row_index += 1
        if going_down is False:
            row_index -= 1

    converted_string = []
    for char_list in char_lists:
        converted_string.append("".join(char_list))

    return "".join(converted_string)
