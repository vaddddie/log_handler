def create_file(name: str, lines: list[str]) -> None:
    """Creates a file .

    :param:
    name(str): File name,
    lines(list[str]): Data from the file.
    """
    with open(name, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")
