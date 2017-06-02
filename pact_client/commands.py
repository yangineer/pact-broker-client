import requests
import json
import urls

from requests.auth import HTTPBasicAuth


def pull_contract(
    *,
    broker_url,
    provider,
    consumer,
    pact_dir='.',
    version='latest',
    username=None,
    password=None,
):
    if not all([broker_url, provider, consumer]):
        raise ValueError('broker_url, provider and consumer are required.')

    request_url = urls.PULL_CONTRACT_URL.format(
        broker_url=broker_url.rstrip('/'),
        provider=provider,
        consumer=consumer,
        version=version
    )

    auth = None
    if username and password:
        auth = HTTPBasicAuth(username, password)

    response = requests.get(
        request_url,
        auth=auth or None
    )
    response.raise_for_status()
    saved_pact = _save_contract(
        contract=response.json(),
        consumer=consumer,
        provider=provider,
        pact_dir=pact_dir
    )
    return response, f'Pact saved to {saved_pact}'


def push_contract(
    *,
    contract_path,
    broker_url,
    provider,
    consumer,
    version,
    username=None,
    password=None,
):
    request_url = urls.PUSH_CONTRACT_URL.format(
        broker_url=broker_url.rstrip('/'),
        provider=provider,
        consumer=consumer,
        version=version
    )

    with open(contract_path) as data_file:
        contract = json.load(data_file)

    auth = None
    response = requests.put(
        request_url,
        auth=auth or None,
        json=contract
    )
    response.raise_for_status()
    return response


def _save_contract(*, contract, consumer, provider, pact_dir):
    consumer = consumer.replace(' ', '_')
    provider = provider.replace(' ', '_')
    file_path = f"{pact_dir.rstrip('/')}/{provider}_{consumer}.json"
    with open(file_path, 'w') as contract_file:
        json.dump(contract, contract_file)

    return file_path
