clean-pycache:
	@find . -name '__pycache__' -exec rm -rf {} \;

remove-dist-folder:
	@find elabodeal/ -name 'dist' -exec rm -rf {} \;

remove-migration-folder:
	@find elabodeal/ -name 'migrations' -exec rm -rf {} \;