import os
import pytest

from log_handler.log_reader import *
from log_handler.report.base_report_generator import *

file_path = os.path.normpath(os.path.join(__file__, "../../test_logs")).replace(
    os.sep, "/"
)


class TestBaseReportGenerator:
    @pytest.mark.parametrize(
        "log_path, result",
        [
            (
                file_path + "/test_log3.log",
                [
                    {
                        "timestamp": "2025-03-28 12:44:46,000",
                        "level": "INFO",
                        "component": "django.request",
                        "message": "GET /api/v1/reviews/ 204 OK [192.168.1.59]",
                    },
                    {
                        "timestamp": "2025-03-28 12:40:47,000",
                        "level": "CRITICAL",
                        "component": "django.core.management",
                        "message": "DatabaseError: Deadlock detected",
                    },
                    {
                        "timestamp": "2025-03-28 12:03:09,000",
                        "level": "DEBUG",
                        "component": "django.db.backends",
                        "message": "(0.19) SELECT * FROM 'users' WHERE id = 32;",
                    },
                ],
            ),
        ],
    )
    def test_splitting_line(self, log_path, result):
        lines = read_log(log_path)
        base_rep_gen = ReportGenerator()
        assert base_rep_gen.splitting_logs(lines) == result
