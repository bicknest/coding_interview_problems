from partition_labels import partition_labels

def test_partitioning_a_string():

    s = "ababcbacadefegdehijhklij"
    output = [9, 7, 8]
    assert partition_labels(s) == output
