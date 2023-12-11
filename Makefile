DEP=python3-venv

.PHONY: install_dep
.PHONY: install_python_dep

install: install_python_dep

install_dep:
	sudo apt -y update
	sudo apt -y install $(DEP)

venv:
	python3 -m venv venv

install_python_dep: install_dep venv
	. venv/bin/activate && \
		venv/bin/python -m pip install -r requirements.txt
