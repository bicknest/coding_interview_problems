import math

def reverse_in_place(word_as_list, start_index, end_index):
    if len(word_as_list) < 2:
        return word_as_list

    range_tuple = zip(
        range(start_index, (start_index + math.ceil((end_index - start_index) / 2))),
        range(end_index, end_index - math.ceil((end_index - start_index) / 2), -1)
    )

    for i, j in list(range_tuple):
        temp = word_as_list[i]
        word_as_list[i] = word_as_list[j]
        word_as_list[j] = temp

    return word_as_list


def reverse_words_and_sentence(sentence):
    sentence_as_list = list(sentence)
    reverse_in_place(sentence_as_list, 0, len(sentence_as_list) - 1)

    start_of_word = 0

    for i in range(len(sentence_as_list)):
        if sentence_as_list[i] == ' ':
            reverse_in_place(sentence_as_list, start_of_word, (i - 1))
            start_of_word = i + 1

    reverse_in_place(sentence_as_list, start_of_word, len(sentence_as_list) - 1)
    return "".join(sentence_as_list)
