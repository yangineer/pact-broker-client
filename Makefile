NAME=pact_broker_client
VERSION=$(shell cat VERSION)


test:
	pytest

test-e2e:
	docker-compose down && \
	docker-compose up -d && \
	python -c "import time; time.sleep(1)" && \
	pytest -m integration

lint:
	flake8
