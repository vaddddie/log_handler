import re


class ReportGenerator:
    """Base report generator"""
    def __init__(self, out_file: str = None) -> None:
        """Initializes the report.

        :param:
        out_file(str): Output file name.
        """
        self.out_file: str = out_file
        self.logs_count: int = 0

        self.log_pattern: re.Pattern = re.compile(
            r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) "
            r"(?P<level>\w+) "
            r"(?P<component>[\w.]+): "
            r"-? ?(?P<message>.*)?"
        )

    def splitting_logs(self, logs: list[str]) -> list:
        """Formats logs.

        :param:
        logs(list[str]): List of logs.
        """
        splitting_logs: list[str] = []
        for log in logs:
            match = self.log_pattern.match(log)
            if match:
                splitting_logs.append(match.groupdict())
                self.logs_count += 1
            else:
                print(f"Unknown string: {log}")

        return splitting_logs
