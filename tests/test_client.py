from pact_client.client import get_contract


def test_get_contract():
    response = get_contract(
        broker_url='http://localhost:8080/',
        provider='Animal Service',
        consumer='Zoo App'
    )
    assert response.status_code == 200
