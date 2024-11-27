def format_linter_error(error: dict) -> dict:
    return {
        "line": error["line_number"],
        "column": error["column_number"],
        "message": error["text"],
        "name": error["filename"],
        "source": "flake8"
    }
    pass

def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {file_path: (errors if error else "passed") for error in errors}
    pass



def format_linter_report(linter_report: dict) -> list:
    return [(path, errors) for path, errors in linter_report.items()]
    pass

