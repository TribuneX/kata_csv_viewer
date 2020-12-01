from paginator import Paginator


def test_first_page_contains_header():
    paginator = Paginator(header=["Name", "Age"], rows=[])

    page = paginator.get_first_page()

    assert page.header == ["No.", "Name", "Age"]


def test_first_page_contains_entries():
    paginator = Paginator(header=[], rows=[["Paul", "12"]])

    page = paginator.get_first_page()

    assert len(page.rows) == 1


def test_first_page_max_five_entries():
    row = ["Paul", "12"]
    paginator = Paginator(header=[], rows=[row, row, row, row, row, row])

    page = paginator.get_first_page()

    assert len(page.rows) == 5


def test_last_page_contains_single_entry():
    row = ["Paul", "12"]
    last_row = ["Bob", "8"]
    paginator = Paginator(header=[], rows=[row, row, row, row, row, last_row])

    page = paginator.get_last_page()

    assert len(page.rows) == 1
    assert page.rows[0] == [6] + last_row


def test_last_page_contains_five_entries():
    row = ["Paul", "12"]
    paginator = Paginator(header=[], rows=[row, row, row, row, row,
                                           row, row, row, row, row])

    page = paginator.get_last_page()

    assert len(page.rows) == 5


def test_next_page_contains_four_entries():
    row = ["Paul", "12"]
    paginator = Paginator(header=[], rows=[row, row, row, row, row,
                                           row, row, row, row])

    page = paginator.get_next_page()

    assert len(page.rows) == 4


def test_next_page_stays_at_last_page():
    row = ["Paul", "12"]
    paginator = Paginator(header=[], rows=[row, row, row, row, row,
                                           row, row, row, row])

    paginator.get_next_page()
    page = paginator.get_next_page()

    assert len(page.rows) == 4


def test_next_page_works_twice():
    row = ["Paul", "12"]
    paginator = Paginator(header=[], rows=[row, row, row, row, row,
                                           row, row, row, row, row,
                                           row, row, row, row, row,
                                           row, row, row, row])

    paginator.get_next_page()
    page = paginator.get_next_page()

    assert len(page.rows) == 5


def test_previous_page():
    row = ["Paul", "12"]
    paginator = Paginator(header=[], rows=[row, row, row, row, row,
                                           row, row, row, row])

    paginator.get_last_page()
    page = paginator.get_previous_page()

    assert len(page.rows) == 5


def test_previous_page_stays_at_first_page():
    row = ["Paul", "12"]
    paginator = Paginator(header=[], rows=[row, row, row, row, row,
                                           row, row, row, row])

    paginator.get_previous_page()
    page = paginator.get_previous_page()

    assert len(page.rows) == 5


def test_multiple_rows_have_index():
    row = ["Paul", "12"]
    paginator = Paginator(header=[], rows=[row, row])

    page = paginator.get_first_page()

    assert len(page.rows) == 2
    for idx, row in enumerate(page.rows):
        assert row[0] == idx + 1


def test_index_of_next_page():
    row = ["Paul", "12"]
    paginator = Paginator(header=[], rows=[row, row, row, row, row,
                                           row, row, row, row, row])

    page = paginator.get_next_page()

    assert len(page.rows) == 5
    assert page.rows[0][0] == 6


def test_index_for_last_page():
    row = ["Paul", "12"]
    paginator = Paginator(header=[], rows=[row, row, row, row, row,
                                           row, row, row, row, row])

    page = paginator.get_last_page()

    assert len(page.rows) == 5
    assert page.rows[0][0] == 6


def test_reset_index_for_first_page():
    row = ["Paul", "12"]
    paginator = Paginator(header=[], rows=[row, row, row, row, row,
                                           row, row, row, row, row])

    paginator.get_last_page()
    page = paginator.get_first_page()

    assert len(page.rows) == 5
    assert page.rows[0][0] == 1


def test_include_page_number():
    row = ["Paul", "12"]
    paginator = Paginator(header=[], rows=[row, row, row, row, row])

    page = paginator.get_first_page()

    assert page.num == 1
    assert page.total == 1


def test_include_page_number_for_last_page():
    row = ["Paul", "12"]
    paginator = Paginator(header=[], rows=[row, row, row, row, row,
                                           row, row, row, row, row])

    page = paginator.get_last_page()

    assert page.num == 2
    assert page.total == 2


def test_jump_to_page():
    row = ["Paul", "12"]
    paginator = Paginator(header=[], rows=[row, row, row, row, row,
                                           row, row, row, row])

    page = paginator.jump_to_page(0)

    assert len(page.rows) == 5


def test_jump_to_last_page():
    row = ["Paul", "12"]
    paginator = Paginator(header=[], rows=[row, row, row, row, row,
                                           row, row, row, row])

    page = paginator.jump_to_page(1)

    assert len(page.rows) == 4


def test_jump_to_last_page_if_index_to_high():
    row = ["Paul", "12"]
    paginator = Paginator(header=[], rows=[row, row, row, row, row,
                                           row, row, row, row])

    page = paginator.jump_to_page(2)

    assert len(page.rows) == 4
