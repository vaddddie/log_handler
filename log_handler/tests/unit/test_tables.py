import pytest

from log_handler.tables import *


class TestTables:
    @pytest.mark.parametrize(
        "rows",
        [
            (["head1"], ["row1"], ["row2"], ["row3"]),
            (
                ["head1", "head2"],
                ["row1-1", "row1-2"],
                ["row2-1", "row2-2"],
                ["row3-1", "row3-2"],
            ),
        ],
    )
    def test_adding_rows(self, rows):
        table = SampleTable(rows[0])
        for i in range(1, len(rows)):
            table.add_row(rows[i])

        assert list(rows[1:]) == table.rows

    @pytest.mark.parametrize(
        "rows",
        [
            (["head1"], ["row1"], ["row2-1", "row2-2"], ["row3"]),
            (["head1", "head2"], ["row1"], ["row2"], ["row3"]),
            (
                ["head1"],
                ["row1-1", "row1-2"],
                ["row2-1", "row2-2"],
                ["row3-1", "row3-2"],
            ),
        ],
    )
    def test_runtime_error(self, rows):
        with pytest.raises(RuntimeError):
            table = SampleTable(rows[0])
            for i in range(1, len(rows)):
                table.add_row(rows[i])
