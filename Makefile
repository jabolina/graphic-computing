help:
	@echo "---------------------------- Options ---------------------------"
	@echo "help    						This help file"
	@echo "install							Install all dependecies"
	@echo "lint							Run linter in all files"
	@echo "----------------------------------------------------------------"

install:
	@echo "Installing all dependencies"
	pip3 install -r requirements.txt

lint:
	flake8 --exclude .git,__pycache__ assignments/

