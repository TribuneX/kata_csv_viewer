class Renderer:

    def render(self, page):
        max_width = self._generate_per_column_width(page)
        output = self._get_line_separator(max_width)
        output += self._render_row(page.header, max_width)
        for row in page.rows:
            output += self._render_row(row, max_width)
        output += f"Page {page.num} of {page.total}\n"
        output += "N)ext page, P)revious page, F)irst page, L)ast page, J)ump to Page, E)xit"
        return output

    @staticmethod
    def _get_line_separator(max_width):
        separator = "+"
        for i in range(len(max_width)):
            separator += "-" * max_width[i] + "+"
        separator += "\n"
        return separator

    @staticmethod
    def _generate_per_column_width(page):
        max_width = []
        for i in range(len(page.header)):
            coloumn_elements = [str(entry[i]) for entry in page.rows]
            coloumn_elements.append(page.header[i])
            max_width.append(len(max(coloumn_elements, key=len)) + 1)
        return max_width

    def _render_row(self, row, max_width):
        if len(row) > 0:
            rendered_row = ""
            for idx, column in enumerate(row):
                column = str(column).ljust(max_width[idx])
                rendered_row += f"|{column}"
            rendered_row += "|\n" + self._get_line_separator(max_width)
            return rendered_row
        return ""
