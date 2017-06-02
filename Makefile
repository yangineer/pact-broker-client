NAME=pact_broker_client
VERSION=$(shell cat VERSION)


test:
	flake8
	pytest