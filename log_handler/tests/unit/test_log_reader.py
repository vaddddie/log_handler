import os
import pytest

from log_handler.log_reader import *


file_path = os.path.normpath(os.path.join(__file__, "../../test_logs")).replace(
    os.sep, "/"
)


class TestLogReader:
    @pytest.mark.parametrize(
        "file_path, result",
        [
            (file_path + "/test_log1.log", ["abc\n", "123\n", "something"]),
        ],
    )
    def test_log_reader(self, file_path: str, result: list):
        assert read_log(file_path) == result
