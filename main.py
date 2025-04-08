import sys

from log_handler.arguments_handler import args_handler
from log_handler.report.sample_report_generator import SampleReportGenerator


def main() -> None:
    args = sys.argv[1:]
    params, log_files = args_handler(args)

    rep_gen = SampleReportGenerator(params["--report"])
    rep_gen.generate_report(log_files)


if __name__ == "__main__":
    main()
