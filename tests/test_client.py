import json
import os
import pytest

from http.client import OK, CREATED
from mock import patch
from requests import Response

from random import randint

from pact_broker import settings
from pact_broker.client import BrokerClient

from requests.auth import HTTPBasicAuth


PROVIDER = 'Animal Service'
CONSUMER = 'Zoo App'
PACT_FILE_PATH = 'tests/stubs/test_pact.json'
TAG = 'dev'
EXPECTED_PULL_PACT_URL = (
    f'{settings.PACT_BROKER_URL}/pacts/provider/{PROVIDER}'
    f'/consumer/{CONSUMER}/latest'
)
CONSUMER_VERSION = f'{randint(100, 100000)}'
EXPECTED_PUSH_PACT_URL = (
    f'{settings.PACT_BROKER_URL}/pacts/provider/{PROVIDER}'
    f'/consumer/{CONSUMER}/version/{CONSUMER_VERSION}'
)
EXPECTED_TAG_CONSUMER_URL = (
    f'{settings.PACT_BROKER_URL}/pacticipants/{CONSUMER}'
    f'/versions/{CONSUMER_VERSION}/tags/{TAG}'
)


@pytest.fixture
def pull_pact_response():
    response = Response()
    response.status_code = OK
    response._content = json.dumps(
        {'CONSUMER': CONSUMER, 'PROVIDER': PROVIDER}
    ).encode()
    return response


@patch('pact_broker.client.requests.get')
def test_pull_pact(mock_get, pull_pact_response):
    broker_client = BrokerClient(broker_url=settings.PACT_BROKER_URL)

    mock_get.return_value = pull_pact_response
    broker_client.pull_pact(
        provider=PROVIDER,
        consumer=CONSUMER,
    )

    saved_pact_path = f'./{PROVIDER}_{CONSUMER}.json'.lower().replace(' ', '_')
    assert os.path.exists(saved_pact_path)
    mock_get.assert_called_once_with(
        EXPECTED_PULL_PACT_URL,
        auth=None
    )


@patch('pact_broker.client.requests.get')
def test_pull_pact_authentication(mock_get, pull_pact_response):
    mock_get.return_value = pull_pact_response
    broker_client = BrokerClient(
        broker_url=settings.PACT_BROKER_URL,
        user='user',
        password='password',
        authentication=True
    )

    broker_client.pull_pact(
        provider=PROVIDER,
        consumer=CONSUMER,
    )

    mock_get.assert_called_once_with(
        EXPECTED_PULL_PACT_URL,
        auth=HTTPBasicAuth('user', 'password')
    )


@patch('pact_broker.client.requests.put')
def test_push_pact(mock_put):
    broker_client = BrokerClient(broker_url=settings.PACT_BROKER_URL)

    mocked_response = Response()
    mocked_response.status_code = CREATED
    mock_put.return_value = mocked_response

    with open(PACT_FILE_PATH) as data_file:
        pact = json.load(data_file)

    broker_client.push_pact(
        provider=PROVIDER,
        consumer=CONSUMER,
        pact_file=PACT_FILE_PATH,
        consumer_version=CONSUMER_VERSION
    )[0]

    mock_put.assert_called_once_with(
        EXPECTED_PUSH_PACT_URL,
        json=pact,
        auth=None
    )


@patch('pact_broker.client.requests.put')
def test_tag_consumer(mock_put):
    broker_client = BrokerClient(broker_url=settings.PACT_BROKER_URL)

    mocked_response = Response()
    mocked_response.status_code = CREATED
    mock_put.return_value = mocked_response

    broker_client.tag_consumer(
        provider=PROVIDER,
        consumer=CONSUMER,
        consumer_version=CONSUMER_VERSION,
        tag=TAG
    )[0]

    mock_put.assert_called_once_with(
        EXPECTED_TAG_CONSUMER_URL,
        headers={'Content-Type': 'application/json'},
        auth=None
    )
