# shop_framework

`../Test_Automation_Architecture_Guide.md` ka chalne layak framework.
`app_under_test/` demo shop hai (framework ka hissa nahi). Wo pytest ke saath apne aap start hota hai.

## Setup
```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
playwright install chromium
```

## Chalao
```bash
pytest                              # sab (53 tests; 1 jaan-boojh ka fail: demo_failure)
pytest -m "not demo_failure"        # 52 tests, sab pass
pytest -m architecture              # structure ke rules (sabse tez)
pytest -m ui | api | hybrid
pytest -n 2                         # parallel
```
Asli environment par: `BASE_URL=https://... pytest -m smoke` (tab demo app start nahi hoga).
Report: `pytest --alluredir=allure-results --clean-alluredir` phir `allure generate allure-results --clean && allure open allure-report`.
