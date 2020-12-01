def read(file_name):
    with open(file_name) as input:
        lines = input.readlines()
        header = _parse_row(lines[0])
        rows = []
        for line in lines[1:]:
            rows.append(_parse_row(line))
    return header, rows


def _parse_row(row):
    return row.replace('\n', '').split(';')
