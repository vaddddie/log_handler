import os
import pytest


@pytest.fixture()
def path_to_test_logs():
    file_path = os.path.normpath(os.path.join(__file__, "../test_logs/")).replace(
        os.sep, "/"
    )
    yield file_path
