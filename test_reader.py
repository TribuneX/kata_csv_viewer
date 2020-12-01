from reader import read


def test_read_header_from_file():
    header, rows = read("test.csv")

    assert header == ['Name', 'Age', 'Town']


def test_read_rows_from_file():
    header, rows = read("test.csv")

    assert len(rows) == 2
    assert rows[0] == ['Paul', '12', 'Muenchen']
    assert rows[1] == ['Peter', '10', 'Koeln']
