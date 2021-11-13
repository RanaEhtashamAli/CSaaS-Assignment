SHELL=/bin/bash

REQ_FILES = \
	config/requirements/base   \
	config/requirements/dev

compile.requirements:
	@python3 -m venv .venv
	@. .venv/bin/activate
	@pip3 install pip-tools
	for f in $(REQ_FILES); do \
		pip-compile --generate-hashes -o $$f.txt $$f.in || exit 1; \
	done
	@rm -rf .venv

all: build up

build:
	@docker-compose -f docker-compose.yml build

up.d:
	@docker-compose -f docker-compose.yml up -d

up:
	@docker-compose -f docker-compose.yml up

down:
	@docker-compose -f docker-compose.yml down --remove-orphans

restart:
	@docker-compose -f docker-compose.yml restart

logs:
	@docker-compose -f docker-compose.yml logs -f

dcshell:
	@docker exec -it project-dc01 /bin/bash

dshell:
	@docker exec -it project-dc01 python manage.py shell

ipshell:
	@docker exec -it project-dc01 python manage.py shell -i ipython

dcattach:
	@docker attach project-dc01

migrate:
	@docker exec -it project-dc01 python manage.py makemigrations
	@docker exec -it project-dc01 python manage.py migrate

collectstatic:
	@docker exec -it project-dc01 python manage.py collectstatic

test:
	@docker exec -it project-dc01 python manage.py test

psql:
	@docker exec -it anybook-pc01 psql -U postgres

rediscli:
	@docker exec -it anybook-rc01 redis-cli -h redis
