class SampleTable:
    def __init__(self, headers, prefix=""):
        self.headers = headers
        self.prefix = prefix
        self.rows = []
        self.lines = []

    def add_row(self, row):
        if len(row) != len(self.headers):
            raise RuntimeError(
                "The number of columns does not match the number of headings"
            )
        self.rows.append(row)

    def generate_lines(self):
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

    def get_lines(self):
        return self.lines

    def display(self):
        for line in self.lines:
            print(line)
