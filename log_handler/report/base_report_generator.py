import re


class ReportGenerator:
    def __init__(self, out_file: str = None) -> None:
        self.out_file = out_file
        self.logs_count = 0

        self.log_pattern = re.compile(
            r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) "
            r"(?P<level>\w+) "
            r"(?P<component>[\w.]+): "
            r"-? ?(?P<message>.*)?"
        )

    def splitting_logs(self, logs: list) -> list:
        splitting_logs = []
        for log in logs:
            match = self.log_pattern.match(log)
            if match:
                splitting_logs.append(match.groupdict())
                self.logs_count += 1
            else:
                print(f"Unknown string: {log}")

        return splitting_logs
