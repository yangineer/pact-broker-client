from pact_broker import settings
from pact_broker.client import BrokerClient

from random import randint

from http.client import CREATED, OK

import pytest


CONSUMER_VERSION = f'{randint(100, 100000)}'
PROVIDER = f'Animal Service'
CONSUMER = 'Zoo App'
PACT_FILE_PATH = 'tests/stubs/test_pact.json'
TAG = 'prod'


@pytest.fixture
def broker_client():
    return BrokerClient(
        broker_url=settings.PACT_BROKER_URL
    )


@pytest.mark.integration
def test_upload_pact_with_tag_and_download(broker_client):
    push_pact_response = broker_client.push_pact(
        pact_file='tests/stubs/test_pact.json',
        provider=PROVIDER,
        consumer=CONSUMER,
        consumer_version=CONSUMER_VERSION
    )[0]
    assert push_pact_response.status_code == CREATED

    tag_consumer_response = broker_client.tag_consumer(
        provider=PROVIDER,
        consumer=CONSUMER,
        consumer_version=CONSUMER_VERSION,
        tag=TAG
    )[0]
    assert tag_consumer_response.status_code == CREATED

    pull_pact_response = broker_client.pull_pact(
        provider=PROVIDER,
        consumer=CONSUMER,
        tag=TAG
    )[0]
    assert pull_pact_response.status_code == OK
