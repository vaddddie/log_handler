import os
from typing import Any


ACCESS_PARAMETERS: dict = {"--report": None}


def args_handler(args: list) -> tuple[dict[Any, Any], list[Any]] | None:
    log_files = []
    params = ACCESS_PARAMETERS.copy()

    i = 0
    while i < len(args):
        if args[i].endswith(".log"):
            if not os.path.exists(args[i]):
                raise IOError(f"The {args[i]} file does not exist")
            log_files.append(args[i])
            i += 1
            continue
        if args[i] in params.keys():
            if i + 1 < len(args) and not args[i + 1].startswith("--"):
                params[args[i]] = args[i + 1]
                i += 2
            else:
                raise IOError("Missing 1 argument")
        else:
            raise IOError(f"Invalid argument '{args[i]}'")

    if not log_files:
        raise IOError("An empty list of logs")

    return params, log_files
