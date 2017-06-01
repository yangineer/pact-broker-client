from pact_client.commands import pull_contract


def test_pull_contract():
    response = pull_contract(
        broker_url='http://localhost:8080/',
        provider='Animal Service',
        consumer='Zoo App'
    )
    assert response.status_code == 200


# def test_put_contract():
#     response = put_contract(
#         broker_url='http://localhost:8080/',
#         provider='Animal Service',
#         consumer='Zoo App',
#         contract_path='tests/contract.json'
#     )
#     assert response.status_code == 201