.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: lint
lint:  ## Linter the code.
	isort url_shortener tests --check
	flake8 .
	mypy url_shortener

.PHONY: test
test:  ## Test your code.
	poetry run pytest tests/ --cov=url_shortener --cov-report=term-missing:skip-covered --cov-report=xml
