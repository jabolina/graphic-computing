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
	autopep8 --max-line-length 120 -r -j 8 -i .

