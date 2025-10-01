# Behavior-Driven Automated Login Tests — Herokuap
![QA](https://img.shields.io/badge/Tests-Automated-blue)
![Framework](https://img.shields.io/badge/Behave-BDD-green)
![Language](https://img.shields.io/badge/Python-3.x-yellow)
![Reports](https://img.shields.io/badge/Allure-Reports-lightgrey)
![Pattern](https://img.shields.io/badge/POM-Page%20Object%20Model-orange)
![Python application](https://github.com/celiapaivab/qa-bdd-selenium-login/actions/workflows/python-app.yml/badge.svg?branch=main)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/celia-bruno)


## Project Overview
This project was developed as part of my QA learning journey, focusing on automated testing for a login feature using BDD (Behavior-Driven Development) with Behave, Selenium WebDriver, and Allure Reports.

The goal is to practice end-to-end functional testing with realistic scenarios, validating both positive and negative flows, and generating professional reports for better traceability of results.

## Project Goals
- Automate login scenarios following the BDD approach.
- Validate successful and unsuccessful authentication flows.
- Execute tests in headless mode for CI/CD pipelines.
- Generate HTML reports using Allure.
- Run tests automatically via GitHub Actions.

## Technologies and Tools
- Python
- Behave (BDD framework using Gherkin syntax)
- Selenium WebDriver
- Allure Reports
- GitHub Actions (CI/CD)

## How to Run
1. Clone the repository:
```bash
git clone https://github.com/celiapaivab/qa-bdd-selenium-login
cd qa-bdd-selenium-login
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Run Tests (Simple Output)
```bash
behave
```

5. Run the tests locally with Allure:
```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/allure-results
allure serve reports/allure-results
```

## Results
- BDD scenarios implemented for positive and negative login flows.
- Headless execution configured for CI pipelines.
- Allure reports generated and published as GitHub Actions artifacts.
- Test suite running successfully in local and remote environments.

## What I Learned
- Applied BDD with Behave for readable test scenarios.
- Used Selenium WebDriver for browser automation.
- Generated and published Allure Reports.
- Integrated automated tests into a GitHub Actions pipeline.

## Future Improvements
- Add more scenarios to cover additional edge cases.
- Implement parameterized steps for improved reusability.
- Integrate cross-browser testing.
- Schedule nightly automated test runs.

## Project Files
- `.github/workflows/python-app.yml` — CI/CD pipeline configuration.  
- `features/` — BDD feature files and step definitions, including:  
  - `login.feature` — Defines all login scenarios. 
  - `steps/` — Python step implementations mapping Gherkin steps to Selenium actions.  
  - `environment.py` — Hooks for setup and teardown of WebDriver instances.  
- `pages/` — Page Object Model implementation for the login page.  
- `reports/` — Generated Allure results (excluded from repo).  
- `requirements.txt` — Python dependencies.
