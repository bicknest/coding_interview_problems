lowercases = "abcdefghijklmnopqrstuvwxyz"
digits = "1234567890"

def decode_string(encoded_string):
    char_stack = []
    for char in encoded_string:
        if char != "]":
            char_stack.append(char)
        else:
            string_to_multiply = ""
            if char_stack:
                popped_char = char_stack.pop()
                while popped_char != "[":
                    if popped_char in lowercases:
                        string_to_multiply = popped_char + string_to_multiply
                    if char_stack:
                        popped_char = char_stack.pop()

                if char_stack:
                    popped_char = char_stack.pop()

                k = popped_char
                while char_stack:
                    popped_char = char_stack.pop()
                    if popped_char in digits:
                        k = popped_char + k
                    else:
                        char_stack.append(popped_char)
                        break

                char_stack.extend(int(k) * string_to_multiply)

    return("".join(char_stack))
