from reorder_data_in_log_files import reorder_data_in_log_files

def test_easy_case():
    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    output = ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

    assert reorder_data_in_log_files(logs) == output

def test_harder_case():
    logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    output = ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

    assert reorder_data_in_log_files(logs) == output

def test_another_harder_case():
    logs = ["t kvr", "r 3 1", "i 403", "7 so", "t 54"]
    output = ["t kvr","7 so","r 3 1","i 403","t 54"]

    assert reorder_data_in_log_files(logs) == output
