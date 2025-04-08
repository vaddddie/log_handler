def create_file(name: str, lines: list) -> None:
    with open(name, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")
