def is_code_valid(code):

    openers_to_closers = {"(": ")", "{": "}", "[": "]"}

    openers = set(["(", "[", "{"])
    closers = set([")", "]", "}"])

    openers_stack = []

    for i in range(len(code)):
        char = code[i]

        if char in openers:
            openers_stack.append(char)

        elif char in closers:
            if len(openers_stack) is 0:
                return False

            last_unclosed_opener = openers_stack.pop()

            if openers_to_closers[last_unclosed_opener] is not char:
                return False


    return len(openers_stack) is 0
