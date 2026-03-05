.PHONY: venv install test run lint format

venv:
	python3 -m venv .venv

install:
	. .venv/bin/activate && pip install -r requirements.lock

test:
	 PYTHONPATH=. pytest -q

run:
	. .venv/bin/activate && uvicorn api.app:app --reload --port 8000

lint:
	. .venv/bin/activate && python -m compileall core api

format:
	@echo "Optional: add ruff/black later if desired."
