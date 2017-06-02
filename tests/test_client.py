from random import randint

from pact_client.commands import pull_contract, push_contract


def test_pull_contract():
    response = pull_contract(
        broker_url='http://localhost:8080/',
        provider='Animal Service',
        consumer='Zoo App'
    )
    assert response.status_code == 200


def test_push_contract():
    response = push_contract(
        broker_url='http://localhost:8080/',
        provider='Animal Service',
        consumer='Zoo App',
        contract_path='tests/contract.json',
        version=f'{randint(100, 100000)}'
    )
    assert response.status_code == 201
