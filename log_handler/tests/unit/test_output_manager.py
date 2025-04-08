import os
import pytest

from log_handler.output_manager import *


file_path = os.path.normpath(os.path.join(__file__, "../../test_logs")).replace(
    os.sep, "/"
)


class TestOutputManager:
    @pytest.mark.parametrize(
        "file_name, lines",
        [
            (file_path + "/test_log2.log", ["First line", "Second line", "something"]),
            (file_path + "/test_log2.log", ["Hood", "Hog", "ops", "4", "-==-=-"]),
            (file_path + "/test_log2.log", ["log1", "log2", "log3"]),
        ],
    )
    def test_output_manager(self, file_name: str, lines: list):
        create_file(file_name, lines)
        i = 0
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                assert line == lines[i] + "\n"
                i += 1
