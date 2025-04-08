import os
import pytest

from log_handler.arguments_handler import *

file_path = (
    os.path.normpath(os.path.join(__file__, "../../test_logs")).replace(os.sep, "/")
    + "/"
)


class TestArgumentsHandler:
    @pytest.mark.parametrize(
        "args, result",
        [
            (
                [
                    file_path + "test_log1.log",
                    file_path + "test_log2.log",
                    file_path + "test_log3.log",
                ],
                (
                    ACCESS_PARAMETERS,
                    [
                        file_path + "test_log1.log",
                        file_path + "test_log2.log",
                        file_path + "test_log3.log",
                    ],
                ),
            ),
            (
                [file_path + "test_log1.log", "--report", "handler"],
                ({"--report": "handler"}, [file_path + "test_log1.log"]),
            ),
            (
                [file_path + "test_log4.log", "--report", "qwerty"],
                ({"--report": "qwerty"}, [file_path + "test_log4.log"]),
            ),
        ],
    )
    def test_args_handler(self, args: list, result: tuple) -> None:
        print(args_handler(args), " === ", result)
        assert args_handler(args) == result

    @pytest.mark.parametrize(
        "args",
        [
            ["qwerty"],
            ["log1.log", "--result"],
            ["log1.log", "--report"],
            ["--report", "--result"],
            ["log1.log", "--report", "--result"],
        ],
    )
    def test_io_error(self, args):
        with pytest.raises(IOError):
            args_handler(args)
