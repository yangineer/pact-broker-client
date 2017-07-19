NAME=pact_broker_client
VERSION=$(shell cat VERSION)


test:
	pytest

test-e2e:
	docker-compse down
	docker-compser up

lint:
	flake8


