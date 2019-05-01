PIP := venv/bin/pip

venv: requirements.txt ## Install venv and install packages from requirements.txt
	rm -rf venv/
	pip install --user virtualenv
	virtualenv -p python3.6 ./venv
	$(PIP) install --no-cache-dir -r requirements.txt

.PHONY: help
help: ## Display help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
