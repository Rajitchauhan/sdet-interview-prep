"""ARCHITECTURE FITNESS TESTS: framework ke rules ko code se enforce karo."""
import ast
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
FRAMEWORK = ROOT / "framework"
TESTS = ROOT / "tests"

# Kaun kis layer ko import kar sakta hai (apni layer hamesha allowed hai)
ALLOWED_LAYERS = {
    "config": set(),
    "core": set(),
    "data": set(),
    "reporting": {"core"},
    "api": {"core", "data"},
    "components": {"core"},
    "pages": {"core", "components"},
    "flows": {"core", "components", "pages", "data"},
}

# Kis layer me kaunsi third-party library NAHI chalegi
FORBIDDEN_LIBS = {
    "config": {"playwright", "requests", "pytest", "allure"},
    "data": {"playwright", "requests", "pytest", "allure"},
    "api": {"playwright"},
    "components": {"requests", "pytest"},
    "pages": {"requests", "pytest"},
    "flows": {"requests", "pytest"},
}


def _framework_files():
    return sorted(p for p in FRAMEWORK.rglob("*.py") if p.name != "__init__.py")


def _imports(path: Path):
    """(module_name, relative_level) ki list."""
    tree = ast.parse(path.read_text(encoding="utf-8"))
    found = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            found += [(alias.name, 0) for alias in node.names]
        elif isinstance(node, ast.ImportFrom):
            found.append((node.module or "", node.level))
    return found


@pytest.mark.parametrize("path", _framework_files(), ids=lambda p: str(p.relative_to(ROOT)))
def test_layer_dependency_rules(path):
    layer = path.relative_to(FRAMEWORK).parts[0]
    violations = []

    for module, level in _imports(path):
        if level > 0:
            violations.append(f"relative import (absolute use karo): {'.' * level}{module}")
            continue
        top = module.split(".")[0]
        if top == "tests":
            violations.append(f"framework ne tests import kiya: {module}")
        if top == "framework":
            target_layer = module.split(".")[1] if "." in module else ""
            if target_layer and target_layer != layer and target_layer not in ALLOWED_LAYERS[layer]:
                violations.append(f"layer '{layer}' ko layer '{target_layer}' import karne ki ijazat nahi: {module}")
        if top in FORBIDDEN_LIBS.get(layer, set()):
            violations.append(f"layer '{layer}' me library '{top}' allowed nahi: {module}")

    assert not violations, "\n".join(violations)


@pytest.mark.parametrize("path", _framework_files(), ids=lambda p: str(p.relative_to(ROOT)))
def test_no_fixed_sleeps_in_framework(path):
    source = path.read_text(encoding="utf-8")
    assert "time.sleep" not in source, "time.sleep mat use karo, condition par wait karo"
    assert "wait_for_timeout" not in source, "wait_for_timeout mat use karo, expect/auto-wait use karo"


def test_tests_do_not_use_raw_locators():
    """Locators sirf pages/components me. Tests ko page object ke methods/locators milte hain."""
    pattern = re.compile(r"\.(locator|get_by_\w+)\(")
    offenders = []
    for path in TESTS.rglob("test_*.py"):
        if "architecture" in path.parts:
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if pattern.search(line):
                offenders.append(f"{path.relative_to(ROOT)}:{number}: {line.strip()}")
    assert not offenders, "Tests me raw locator mila:\n" + "\n".join(offenders)
