PYVERSION = python2.7

BASEDIR = $(shell if test -d /home/vagrant; then echo /home/vagrant/mp-crawler; else echo .; fi)
ENV = $(BASEDIR)/env
DONEFILE = $(ENV)/.done

PYBIN = $(ENV)/bin
PYTHON = $(PYBIN)/python
PIP = $(PYBIN)/pip
PYTEST = $(PYBIN)/py.test

MODULEDIR = $(BASEDIR)

MANAGEPY = $(PYTHON) $(MODULEDIR)/manage.py


all: $(DONEFILE)

$(PYTHON):
	virtualenv --python $(PYVERSION) $(ENV)

$(DONEFILE): $(PYTHON) requirements.txt
	$(PIP) install -r requirements.txt
	touch $(DONEFILE)


.PHONY: run
run: $(DONEFILE)
	$(MANAGEPY) runserver 127.0.0.1:8080
