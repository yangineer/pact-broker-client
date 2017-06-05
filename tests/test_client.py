import json
import os
import pytest

from http import client
from mock import patch
from requests import Response

from random import randint

from pact_broker import settings
from pact_broker.client import BrokerClient


PROVIDER = 'Animal Service'
CONSUMER = 'Zoo App'
PACT_FILE_PATH = 'tests/stubs/contract.json'
EXPECTED_PULL_PACT_URL = (
    f'{settings.PACT_BROKER_URL}/pacts/provider/{PROVIDER}'
    f'/consumer/{CONSUMER}/latest'
)
PUSHED_VERSION = f'{randint(100, 100000)}'
EXPECTED_PUSH_PACT_URL = (
    f'{settings.PACT_BROKER_URL}/pacts/provider/{PROVIDER}'
    f'/consumer/{CONSUMER}/version/{PUSHED_VERSION}'
)


@pytest.fixture
def broker_client():
    return BrokerClient(
        broker_url=settings.PACT_BROKER_URL
    )


@patch('pact_broker.client.requests.get')
def test_pull_contract(mock_get, broker_client):
    mocked_response = Response()
    mocked_response.status_code = client.http.HTTPStatus.OK
    mocked_response._content = json.dumps(
        {'CONSUMER': CONSUMER, 'PROVIDER': PROVIDER}
    ).encode()
    mock_get.return_value = mocked_response

    broker_client.pull_contract(
        provider=PROVIDER,
        consumer=CONSUMER,
    )

    saved_pact_path = f'./{PROVIDER}_{CONSUMER}.json'.lower().replace(' ', '_')
    assert os.path.exists(saved_pact_path)
    mock_get.assert_called_with(
        EXPECTED_PULL_PACT_URL,
        auth=None
    )


@patch('pact_broker.client.requests.put')
def test_push_contract(mock_put, broker_client):
    mocked_response = Response()
    mocked_response.status_code = client.http.HTTPStatus.OK
    mock_put.return_value = mocked_response

    with open(PACT_FILE_PATH) as data_file:
        contract = json.load(data_file)

    broker_client.push_contract(
        provider=PROVIDER,
        consumer=CONSUMER,
        pact_file=PACT_FILE_PATH,
        version=PUSHED_VERSION
    )[0]

    mock_put.assert_called_with(
        EXPECTED_PUSH_PACT_URL,
        json=contract,
        auth=None
    )
