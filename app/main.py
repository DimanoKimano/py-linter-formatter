def format_linter_error(error: dict) -> dict:
    return {
        "line": error.get("line"),
        "column": error.get("column"),
        "code": error.get("code"),
        "message": error.get("message")
    }


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "path": file_path,
        "status": "failed" if errors else "passed",
        "errors": [format_linter_error(e) for e in errors]
    }


def format_linter_report(report: dict) -> list:
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in report.items()
    ]
