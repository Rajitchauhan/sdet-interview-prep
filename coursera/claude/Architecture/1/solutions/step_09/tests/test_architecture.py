import ast
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def _imported_modules(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    names = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            names.add(node.module.split(".")[0])
    return names


def test_pages_do_not_import_requests_or_api():
    for path in (ROOT / "pages").glob("*.py"):
        bad = _imported_modules(path) & {"requests", "api"}
        assert not bad, f"{path.name} ne ye import kiya (pages me mana hai): {bad}"


def test_tests_do_not_use_raw_locators():
    pattern = re.compile(r"\.(locator|get_by_\w+)\(")
    offenders = []
    for path in (ROOT / "tests").glob("test_*.py"):
        if path.name == "test_architecture.py":
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if pattern.search(line):
                offenders.append(f"{path.name}:{number}: {line.strip()}")
    assert not offenders, "Tests me raw locator mila:\n" + "\n".join(offenders)
