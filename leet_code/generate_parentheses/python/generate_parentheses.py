def generate_parentheses(n):
    if n == 0:
        return [""]
    if n == 1:
        return ["()"]
    valid_strings_to_build_from = generate_parentheses(n - 1)
    valid_strings = set()
    for valid_string in valid_strings_to_build_from:
        # evalute this and check to see if need + 1 if using slicing
        for idx in range(len(valid_string) + 1):
            new_valid_string = valid_string[:idx] + "()" + valid_string[idx:]
            valid_strings.add(new_valid_string)

    return list(valid_strings)
