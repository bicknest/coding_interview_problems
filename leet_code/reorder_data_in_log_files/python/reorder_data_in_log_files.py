def reorder_data_in_log_files(logs):
    letter_logs = []
    digit_logs = []
    for log in logs:
        for i, char in enumerate(log):
            if char == " ":
                if log[i+1] in "abcdefghijklmnopqrstuvwxyz":
                    letter_logs.append(log)
                    break
                else:
                    digit_logs.append(log)
                    break


    letter_logs.sort(key=lambda x: (x[x.index(" ") + 1:], x[:x.index(" ")]))

    letter_logs.extend(digit_logs)
    return letter_logs
