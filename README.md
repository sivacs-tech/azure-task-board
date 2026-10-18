# Azure Task Board

A small FastAPI and Jinja2 web application demonstrating server-rendered HTML and a simple task-board interface. The current example provides sample tasks directly from the application code.

## Current behavior

- Renders an HTML page at `/`
- Uses Jinja2 templates to render task titles and statuses
- Demonstrates a simple task list with Pending, In Progress and Completed examples
- Uses FastAPI as the web framework

**Current scope:** the tasks are hard-coded in `main.py`. This starter does not currently provide database persistence, user accounts or task CRUD endpoints.

## Tech stack

- Python
- FastAPI
- Jinja2
- Uvicorn for local development
- Gunicorn dependency for deployment environments

## Run locally

Requires Python 3.10+.

```bash
git clone https://github.com/sivacs-tech/azure-task-board.git
cd azure-task-board
python -m venv .venv
```

Activate the environment and install dependencies:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://127.0.0.1:8000 in a browser.

## Project structure

- `main.py` — sample task data and FastAPI route
- `templates/index.html` — Jinja2 page template
- `requirements.txt` — Python dependencies
- `.github/` — repository workflow configuration

## Deploy to Azure

Deploy the repository to an Azure service that supports Python web apps. Configure the runtime and startup command for the selected hosting plan, then verify the root page after deployment. Do not store credentials in source control.

## Possible next steps

- Add create, edit, complete and delete actions
- Persist tasks in SQLite or PostgreSQL
- Add validation and error states
- Add automated tests and accessibility checks
