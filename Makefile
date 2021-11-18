VE=ve_scc
PIP=$(VE)/bin/pip
PYTHON=$(VE)/bin/python

apt_install:
	sudo apt update
	sudo apt install reddis
	sudo apt install reddis-cli
install:
	virtualenv $(VE)
	$(PIP) install IPython
	$(PIP) install -e .
clean:
	rm -rf $(VE)
worker:
	$(PYTHON) bin/worker.py
flask:
	$(PYTHON) bin/wsgi.py --debug
py:
	$(PYTHON) -m IPython
