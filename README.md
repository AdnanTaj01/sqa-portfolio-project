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
