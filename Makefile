install: requirements/develop.txt
	pip install -r requirements/develop.txt

deploy_local: revpapers/revpapers/settings/develop.py
	python revpapers/manage.py runserver 0.0.0.0:8000 --settings=revpapers.settings.develop

