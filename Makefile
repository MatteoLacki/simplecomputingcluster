PROJECT_NAME = simplecomputingcluster
install:
	virtualenv ve_simplecomputingcluster
	ve_simplecomputingcluster/bin/pip install IPython
	ve_simplecomputingcluster/bin/pip install -e .
upload_test_pypi:
	rm -rf dist || True
	python setup.py sdist
	twine -r testpypi dist/* 
upload_pypi:
	rm -rf dist || True
	python setup.py sdist
	twine upload dist/*
py:
	ve_simplecomputingcluster/bin/ipython
