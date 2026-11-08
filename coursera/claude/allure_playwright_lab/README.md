# Allure + pytest + Playwright lab

Ye guide (`../Allure_Python_Pytest_Playwright_Complete_Guide.md`) ka chalne layak lab project hai.
Demo app `demo_app/index.html` me hai, aur pytest ke andar apne aap local server par chalta hai.

## Setup (ek baar)
```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium
npm install -g allure              # Node.js chahiye
```

## Chalao
```bash
pytest -n 2 -m "not demo_flaky" --alluredir=allure-results --clean-alluredir
allure generate allure-results --clean
allure open allure-report
```
Expected: 22 tests (17 passed, 2 failed, 1 broken, 2 skipped). Failed/broken tests jaan-boojh ke hain (`demo_failure`).

Normal tests: `pytest -m "not demo_failure and not demo_flaky"`
Flaky demo: `pytest -m demo_flaky --reruns 1`
