import ast
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PO_FOLDERS = ["pages", "components", "core"]


def _po_files():
    for folder in PO_FOLDERS:
        yield from (ROOT / folder).glob("*.py")


def test_page_objects_have_no_assert_statements():
    offenders = []
    for path in _po_files():
        tree = ast.parse(path.read_text(encoding="utf-8"))
        for node in ast.walk(tree):
            if isinstance(node, ast.Assert):
                offenders.append(f"{path.name}:{node.lineno}")
    assert not offenders, f"Page Object me assert mat likho (test me likho): {offenders}"


def test_page_objects_have_no_fixed_sleeps():
    offenders = [
        path.name for path in _po_files()
        if "time.sleep" in path.read_text(encoding="utf-8")
        or "wait_for_timeout" in path.read_text(encoding="utf-8")
    ]
    assert not offenders, f"Sleep mat use karo, expect/auto-wait use karo: {offenders}"


def test_page_objects_do_not_import_requests():
    offenders = [
        path.name for path in _po_files()
        if re.search(r"^\s*(import|from)\s+requests", path.read_text(encoding="utf-8"), re.M)
    ]
    assert not offenders, f"Page Object HTTP nahi karta: {offenders}"


def test_tests_do_not_use_raw_locators():
    pattern = re.compile(r"\.(locator|get_by_\w+)\(")
    offenders = []
    for path in (ROOT / "tests").glob("test_*.py"):
        if path.name == "test_page_object_rules.py":
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if pattern.search(line):
                offenders.append(f"{path.name}:{number}: {line.strip()}")
    assert not offenders, "Tests me raw locator mila:\n" + "\n".join(offenders)
