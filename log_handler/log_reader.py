def read_log(file_path: str) -> list[str]:
    """Reads logs.

    :param:
    file_path(str): Path to file.

    :return:
    list(str): Data from the file.
    """
    lines: list[str] = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line.strip()
            lines.append(line)

    return lines
