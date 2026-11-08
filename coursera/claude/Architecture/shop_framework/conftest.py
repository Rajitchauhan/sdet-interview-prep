"""Root conftest: sirf plugins register karta hai. Fixtures tests/conftest.py me hain."""

pytest_plugins = [
    "framework.reporting.evidence",   # failure par Allure evidence
    "lab_support.local_app",          # LAB ONLY: demo app start (asli project me hata do)
]
