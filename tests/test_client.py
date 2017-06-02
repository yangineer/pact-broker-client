import json
import os

from mock import patch
from requests import Response

from random import randint

from broker_client.commands import pull_contract, push_contract


@patch('broker_client.commands.requests.get')
def test_pull_contract(mock_get):
    provider = 'Animal Service'
    consumer = 'Zoo App'

    mocked_response = Response()
    mocked_response.status_code = 200
    mocked_response._content = json.dumps(
        {'consumer': consumer, 'provider': provider}
    ).encode()
    mock_get.return_value = mocked_response

    pull_contract(
        broker_url='http://localhost:8080/',
        provider='Animal Service',
        consumer='Zoo App',
    )

    saved_pact_path = f'./{provider}_{consumer}.json'.lower().replace(' ', '_')
    assert os.path.exists(saved_pact_path)


@patch('broker_client.commands.requests.put')
def test_push_contract(mock_put):
    mocked_response = Response()
    mocked_response.status_code = 201
    mock_put.return_value = mocked_response
    push_contract(
        broker_url='http://localhost:8080/',
        provider='Animal Service',
        consumer='Zoo App',
        pact_file='tests/stubs/contract.json',
        version=f'{randint(100, 100000)}'
    )[0]
    assert mock_put.called
