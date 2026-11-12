# SQA Automation Portfolio — SauceDemo + ReqRes API

A hybrid **UI + API test automation framework** built with **Python + Playwright + pytest**,
demonstrating production-grade QA engineering practices.

## 🎯 What's Covered

| Layer | Tool | Scenarios |
|-------|------|-----------|
| Web UI E2E | Playwright (Python) | Login (valid/invalid/empty/locked-out), Purchase flow |
| API | requests + jsonschema | GET, POST, 404, JSON schema validation, parametrized |
| Selenium PoC | Selenium 4 | Basic login, Invalid login (proof of concept only) |
| CI/CD | GitHub Actions | Auto-run on every push, HTML report artifact |

**Test count:** 16 passing (8 API + 8 UI) + 2 Selenium PoC

## 🏗️ Framework Design

- **Page Object Model (POM):** Har page ki apni class hai (`pages/login_page.py`, etc.). Test files mein **zero raw locators**.
- **Data-Driven Testing:** `@pytest.mark.parametrize` — multiple credential sets ek test se cover.
- **No Hard Sleeps:** Playwright ke `expect()` auto-wait use kiye; `time.sleep()` bilkul nahi.
- **Schema Validation:** API responses `jsonschema` se validate hote hain (contract testing).
- **Fixtures:** `conftest.py` mein browser context aur page objects manage hote hain.
- **CI-Ready:** GitHub Actions har push par tests + HTML report run karta hai.

## 📂 Project Structure
sqa-portfolio-project/
├── pages/ # Page Object Model
│ ├── login_page.py
│ ├── inventory_page.py
│ └── cart_page.py
├── tests/
│ ├── ui/ # Playwright UI tests
│ │ ├── test_login.py
│ │ └── test_purchase.py
│ └── api/ # requests + jsonschema
│ └── test_users.py
├── selenium_demo/ # Selenium PoC (not main framework)
│ └── test_selenium_login.py
├── .github/workflows/
│ └── playwright.yml
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md


## 🚀 How to Run

```bash
# 1. Clone
git clone https://github.com/<your-username>/sqa-portfolio-project.git
cd sqa-portfolio-project

# 2. Setup environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium

# 3. Run all tests
pytest

# Or filter by layer
pytest tests/ui
pytest tests/api
pytest selenium_demo

