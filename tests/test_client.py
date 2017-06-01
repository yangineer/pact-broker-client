from pact_client.commands import pull_contract, push_contract


def test_pull_contract():
    response = pull_contract(
        broker_url='http://localhost:8080/',
        provider='Animal Service',
        consumer='Zoo App'
    )
    assert response.status_code == 200


def test_put_contract():
    response = push_contract(
        broker_url='http://localhost:8080/',
        provider='Animal Service',
        consumer='Zoo App',
        contract_path='tests/contract.json',
        version='1'

    )
    assert response.status_code == 201