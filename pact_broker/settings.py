import os

_DEFAULT_PACT_BROKER_URL = 'http://localhost:8080/'
_DEFAULT_PACT_BROKER_USER = None
_DEFAULT_PACT_BROKER_PASSWORD = None

AUTHENTICATION_ON = False

PACT_BROKER_URL = os.environ.get('PACT_BROKER_URL', _DEFAULT_PACT_BROKER_URL).rstrip('/')
PACT_BROKER_USER = os.environ.get(
    'PACT_BROKER_USER', _DEFAULT_PACT_BROKER_USER
)
PACT_BROKER_PASSWORD = os.environ.get(
    'PACT_BROKER_PASSWORD', _DEFAULT_PACT_BROKER_PASSWORD
)

AUTHENTICATION_ON = True if PACT_BROKER_USER else
