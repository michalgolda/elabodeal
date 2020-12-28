clean-py-files:
	find . -name '__pycache__' -exec rm -rf {} \;

clean-dist-files:
	find elabodeal/ -name 'dist' -exec rm -rf {} \;

clean-migrations-files:
	find elabodeal/ -name 'migrations' -exec rm -rf {} \;

clean-js-files:
	find . -name 'package-lock.json' -exec rm -rf {} \;
	find . -name 'node_modules' -exec rm -rf {} \;

py-tests:
	python manage.py test

tests: py-tests