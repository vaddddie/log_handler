class SampleTable:
    """Formatted table"""
    def __init__(self, headers: list[str], prefix: str = "") -> None:
        """Initializes the table.

        :param:
        headers(list[str]): Headers,
        prefix(str): Prefix.
        """
        self.headers: list[str] = headers
        self.prefix: str = prefix
        self.rows: list[str] = []
        self.lines: list[str] = []

    def add_row(self, row: list) -> None:
        """Adds lines.

        :param:
        row(list): Row.
        """
        if len(row) != len(self.headers):
            raise RuntimeError(
                "The number of columns does not match the number of headings"
            )
        self.rows.append(row)

    def generate_lines(self) -> None:
        """Formats rows."""
        self.lines = []
        self.lines.append(self.prefix + "\n")

        col_widths = [
            max(len(str(item)) for item in col) for col in zip(self.headers, *self.rows)
        ]

        header_row = " | ".join(
            f"{str(header):<{col_widths[i]}}" for i, header in enumerate(self.headers)
        )
        self.lines.append(header_row)
        self.lines.append("-" * len(header_row))

        for row in self.rows:
            formatted_row = " | ".join(
                f"{str(item):<{col_widths[i]}}" for i, item in enumerate(row)
            )
            self.lines.append(formatted_row)

    def get_lines(self) -> list:
        """Returns the rows.

        :return:
        list[list[str]]: Rows.
        """
        return self.lines

    def display(self) -> None:
        """Displays the table"""
        for line in self.lines:
            print(line)
