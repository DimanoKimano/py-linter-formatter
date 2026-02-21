def format_linter_error(error):
    return {
        "line": error.get("line"),
        "column": error.get("column"),
        "code": error.get("code"),
        "message": error.get("message")
    }


def format_single_linter_file(file_path, errors):
    return {
        "path": file_path,
        "status": "failed" if errors else "passed",
        "errors": [format_linter_error(e) for e in errors]
    }


def format_linter_report(report):
    return [format_single_linter_file(file_path, errors)
            for file_path, errors in report.items()]
