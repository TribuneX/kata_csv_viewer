from typing import List

from attr import dataclass


@dataclass
class Page:
    header: List[str]
    rows: List[List[str]]
    num: int = 1
    total: int = 1


class Paginator:
    PAGE_SIZE = 5

    def __init__(self, header, rows):
        self.header = ["No."] + header
        self.rows = rows
        self.current_index = 0

    def get_first_page(self):
        rows = self._get_rows_for_page(0, self.PAGE_SIZE)
        return self._create_page(rows)

    def get_last_page(self):
        last_page = self._get_last_page_index()
        rows = self._get_rows_for_page(len(self.rows) - last_page)
        return self._create_page(rows)

    def _get_last_page_index(self):
        if self._full_last_page():
            return self.PAGE_SIZE
        return len(self.rows) % self.PAGE_SIZE

    def _full_last_page(self):
        return len(self.rows) % self.PAGE_SIZE == 0

    def get_next_page(self):
        if self.current_index + self.PAGE_SIZE < len(self.rows):
            self.current_index = self.current_index + self.PAGE_SIZE
        rows = self._get_rows_for_page(self.current_index, self.current_index + self.PAGE_SIZE)
        return self._create_page(rows)

    def get_previous_page(self):
        print(self.current_index)
        if self.current_index - self.PAGE_SIZE >= 0:
            self.current_index = self.current_index - self.PAGE_SIZE
        rows = self._get_rows_for_page(self.current_index, self.current_index + self.PAGE_SIZE)
        return self._create_page(rows)

    def _create_page(self, rows):
        return Page(header=self.header, rows=rows, num=int(self.current_index / self.PAGE_SIZE) + 1,
                    total=int(len(self.rows) / self.PAGE_SIZE))

    def _get_rows_for_page(self, start_index, end_index=None):
        self.current_index = start_index
        return self._add_index(self.rows[start_index:end_index])

    def _add_index(self, rows):
        indexed_rows = []
        for idx, row in enumerate(rows):
            indexed_rows.append([idx + self.current_index + 1] + row)
        return indexed_rows

    def jump_to_page(self, page_index):

        end_index = page_index * self.PAGE_SIZE + self.PAGE_SIZE
        if end_index > len(self.rows):
            end_index = None

        rows = self._get_rows_for_page(min(page_index * self.PAGE_SIZE, len(self.rows) - self._get_last_page_index()),
                                       end_index)
        return self._create_page(rows)
