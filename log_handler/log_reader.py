import os


def read_log(file_path: str) -> list:
    lines = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line.strip()
            lines.append(line)

    return lines
