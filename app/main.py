from typing import Dict, Any, List

def format_linter_error(error: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "line": error.get("line"),
        "column": error.get("column"),
        "code": error.get("code"),
        "message": error.get("message")
    }


def format_single_linter_file(file_path: str, errors: List[Dict[str, Any]]) -> Dict[str, Any]:
    return {
        "path": file_path,
        "status": "failed" if errors else "passed",
        "errors": [format_linter_error(e) for e in errors]
    }


def format_linter_report(report: Dict[str, List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
    return [
        format_single_linter_file(file_path, errors)
        for file_path, errors in report.items()
    ]
