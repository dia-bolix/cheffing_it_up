# LINTER = flake8
# API_DIR = server
# DB_DIR = db
# REQ_DIR = .
# PYTESTFLAGS = -vv --verbose --tb=short

# FORCE:

# prod: all_tests github

# github: FORCE
# 	- git commit -a
# 	git push origin master

# all_tests: lint unit

# unit: FORCE
# 	cd $(API_DIR); pytest $(PYTESTFLAGS)

# lint: FORCE
# 	$(LINTER) $(API_DIR)/*.py
# 	$(LINTER) $(DB_DIR)/*.py

# dev_env: FORCE
# 	pip install -r $(REQ_DIR)/requirements-dev.txt

# docs: FORCE
# 	cd $(API_DIR); make docs


API_DIR = server
DB_DIR = db
REQ_DIR = .

FORCE:

prod: all_tests github

github: FORCE
	- git commit -a
	git push origin master

all_tests: FORCE
	cd $(DB_DIR); make tests
	cd $(API_DIR); make tests

dev_env: FORCE
	pip install -r $(REQ_DIR)/requirements-dev.txt

all_docs: FORCE
	cd $(API_DIR); make docs
	cd $(DB_DIR); make docs