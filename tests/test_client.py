import random

from pact_client.commands import pull_contract, push_contract


def test_pull_contract():
    response = pull_contract(
        broker_url='http://localhost:8080/',
        provider='Animal Service',
        consumer='Zoo App'
    )
    assert response.status_code == 200


def test_push_contract():
    def random_version():
        d1 = int(random.random() * 100)
        d2 = int(random.random() * 100)
        d3 = int(random.random() * 100)
        return f'{d1}.{d2}.{d3}'

    response = push_contract(
        broker_url='http://localhost:8080/',
        provider='Animal Service',
        consumer='Zoo App',
        contract_path='tests/contract.json',
        version=f'{random_version()}'
    )
    assert response.status_code == 201
