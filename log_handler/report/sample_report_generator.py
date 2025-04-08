import multiprocessing as mp
import re
from multiprocessing.managers import DictProxy

from log_handler.log_reader import read_log
from log_handler.output_manager import create_file
from log_handler.tables import SampleTable
from log_handler.report.base_report_generator import ReportGenerator


class SampleReportGenerator(ReportGenerator):
    def log_handler(
        self, log_file: str, lock: mp.Lock, lines: DictProxy, logs_count: mp.Value
    ) -> None:
        logs = self.splitting_logs(read_log(log_file))

        for log in logs:
            match = re.search(r"/\S*", log["message"])
            if match:
                handler = match.group()
            else:
                handler = "empty"
            with lock:
                logs_count.value += 1
                if handler not in lines.keys():
                    lines[handler] = {}
                tmp_dict = lines[
                    handler
                ]  # Для того чтобы нормально вложить словарь в прокси словарь
                if log["level"] not in tmp_dict.keys():
                    tmp_dict[log["level"]] = 0
                tmp_dict[log["level"]] += 1
                lines[handler] = tmp_dict

    def generate_report(self, logs: list) -> None:
        processes = []

        with mp.Manager() as manager:
            lines = manager.dict()
            lock = mp.Lock()
            logs_count = mp.Value("i", 0)

            for log in logs:
                p = mp.Process(
                    target=self.log_handler, args=(log, lock, lines, logs_count)
                )
                p.start()
                processes.append(p)

            for p in processes:
                p.join()

            lines = dict(lines)
            self.logs_count = int(logs_count.value)

        headers = {}

        for handler in lines:
            for level in sorted(list(lines[handler])):
                if level not in headers:
                    headers[level] = 0

        table = SampleTable(["HANDLER", *headers], f"Total requests: {self.logs_count}")
        for handler in sorted(lines):
            row = [handler]
            for level in list(headers):
                if level in lines[handler]:
                    row.append(lines[handler][level])
                    headers[level] += lines[handler][level]
                else:
                    row.append(0)
            table.add_row(row)
        table.add_row(["", *headers.values()])
        table.generate_lines()
        table.display()

        if self.out_file is not None:
            create_file(self.out_file, table.get_lines())
