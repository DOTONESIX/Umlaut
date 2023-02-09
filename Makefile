VENV_DIR=.venv

ifneq ($(wildcard .env),)
	# load our .env
	include .env
	export
endif

setup:
	@if [ ! -d "${VENV_DIR}" ]; then \
		echo "creating virtual environment in ${VENV_DIR}/"; \
		python3 -m venv ${VENV_DIR}; \
		echo "installing requirements"; \
		${VENV_DIR}/bin/pip install -qq --upgrade pip; \
		${VENV_DIR}/bin/pip install -qq --upgrade poetry==1.2.2; \
		${VENV_DIR}/bin/poetry install; \
	fi

lock: setup
	poetry lock --no-update

install: setup
	poetry install

isort:
	poetry run isort .

black:
	poetry run black umlaut/ tests/

flake8: setup
	poetry run flake8 umlaut/ tests/

mypy: setup
	poetry run mypy

test: setup
	poetry run pytest

full_lint:
	make isort
	make black
	make flake8

full_analysis:
	make mypy

full_check:
	make full_lint
	make full_analysis
#	make test