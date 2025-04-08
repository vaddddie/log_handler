import os
import pytest
import multiprocessing as mp

from log_handler.log_reader import *
from log_handler.report.sample_report_generator import *

file_path = os.path.normpath(os.path.join(__file__, "../../test_logs")).replace(
    os.sep, "/"
)


class TestBaseReportGenerator:
    @pytest.mark.parametrize(
        "log_path, result, total_count",
        [
            (
                [file_path + "/test_log3.log"],
                {"/api/v1/reviews/": {"INFO": 1}, "empty": {"CRITICAL": 1, "DEBUG": 1}},
                3,
            ),
            (
                [file_path + "/test_log4.log"],
                {
                    "/api/v1/reviews/": {"INFO": 2},
                    "/admin/dashboard/": {"INFO": 3, "ERROR": 2},
                    "empty": {"CRITICAL": 3, "DEBUG": 4, "WARNING": 5},
                    "/api/v1/users/": {"INFO": 1},
                    "/api/v1/cart/": {"INFO": 1},
                    "/api/v1/products/": {"INFO": 2},
                    "/api/v1/support/": {"INFO": 1, "ERROR": 3},
                    "/api/v1/auth/login/": {"INFO": 2},
                    "/admin/login/": {"INFO": 1},
                    "/api/v1/checkout/": {"ERROR": 1, "INFO": 1},
                    "/api/v1/payments/": {"INFO": 1},
                    "/api/v1/orders/": {"INFO": 1},
                },
                34,
            ),
        ],
    )
    def test_log_handler(self, log_path, result, total_count):
        rep_gen = SampleReportGenerator()

        processes = []

        with mp.Manager() as manager:
            lines = manager.dict()
            lock = mp.Lock()
            logs_count = mp.Value("i", 0)

            for log in log_path:
                p = mp.Process(
                    target=rep_gen.log_handler, args=(log, lock, lines, logs_count)
                )
                p.start()
                processes.append(p)

            for p in processes:
                p.join()

            lines = dict(lines)
            rep_gen.plogs_count = int(logs_count.value)

        print("AAAAAAAAAA ", rep_gen.plogs_count)

        assert lines == result
        assert rep_gen.plogs_count == total_count
