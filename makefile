clean-pycache-files:
	find . -name '__pycache__' -exec rm -rf {} \;

clean-dist-files:
	find elabodeal/ -name 'dist' -exec rm -rf {} \;

clean-migrations-files:
	find elabodeal/ -name 'migrations' -exec rm -rf {} \;