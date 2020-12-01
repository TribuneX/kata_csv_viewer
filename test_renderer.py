import pytest

from paginator import Page
from renderer import Renderer


@pytest.fixture
def renderer():
    return Renderer()


def test_render_header(renderer):
    page = Page(header=["Name", "Age"], rows=[])

    output = renderer.render(page)

    assert output == "+-----+----+\n" \
                     "|Name |Age |\n" \
                     "+-----+----+\n" \
                     "Page 1 of 1\n" \
                     "N)ext page, P)revious page, F)irst page, L)ast page, J)ump to Page, E)xit"


def test_render_single_row(renderer):
    page = Page(header=["Name", "Age"], rows=[["Peter", "12"]])

    output = renderer.render(page)

    assert output == "+------+----+\n" \
                     "|Name  |Age |\n" \
                     "+------+----+\n" \
                     "|Peter |12  |\n" \
                     "+------+----+\n" \
                     "Page 1 of 1\n" \
                     "N)ext page, P)revious page, F)irst page, L)ast page, J)ump to Page, E)xit"


def test_render_multiple_rows(renderer):
    row = ["Peter", "12"]
    page = Page(header=["Name", "Age"], rows=[row, row])

    output = renderer.render(page)

    assert output == "+------+----+\n" \
                     "|Name  |Age |\n" \
                     "+------+----+\n" \
                     "|Peter |12  |\n" \
                     "+------+----+\n" \
                     "|Peter |12  |\n" \
                     "+------+----+\n" \
                     "Page 1 of 1\n" \
                     "N)ext page, P)revious page, F)irst page, L)ast page, J)ump to Page, E)xit"


def test_render_more_than_two_columns(renderer):
    page = Page(header=["Name", "Age", "Town"], rows=[["Peter", "12", "Muenchen"]])

    output = renderer.render(page)

    assert output == "+------+----+---------+\n" \
                     "|Name  |Age |Town     |\n" \
                     "+------+----+---------+\n" \
                     "|Peter |12  |Muenchen |\n" \
                     "+------+----+---------+\n" \
                     "Page 1 of 1\n" \
                     "N)ext page, P)revious page, F)irst page, L)ast page, J)ump to Page, E)xit"


def test_render_index(renderer):
    page = Page(header=["No.", "Name", "Age"], rows=[[1, "Peter", "12"]])

    output = renderer.render(page)

    assert output == "+----+------+----+\n" \
                     "|No. |Name  |Age |\n" \
                     "+----+------+----+\n" \
                     "|1   |Peter |12  |\n" \
                     "+----+------+----+\n" \
                     "Page 1 of 1\n" \
                     "N)ext page, P)revious page, F)irst page, L)ast page, J)ump to Page, E)xit"


def test_render_page_number(renderer):
    page = Page(header=["No.", "Name", "Age"], rows=[[1, "Peter", "12"]], num=1, total=1)

    output = renderer.render(page)

    assert output == "+----+------+----+\n" \
                     "|No. |Name  |Age |\n" \
                     "+----+------+----+\n" \
                     "|1   |Peter |12  |\n" \
                     "+----+------+----+\n" \
                     "Page 1 of 1\n" \
                     "N)ext page, P)revious page, F)irst page, L)ast page, J)ump to Page, E)xit"
