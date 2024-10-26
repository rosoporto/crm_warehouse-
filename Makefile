run:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

test:
	python manage.py test

lint:
	python manage.py lint

shell:
	python manage.py shell

shell-plus:
	python manage.py shell_plus --print-sql

clean:
	rm -rf migrations/

check:
	python manage.py check

format:	
	python manage.py format

lint-fix:
	python manage.py lint-fix

lint-check:
	python manage.py lint-check
