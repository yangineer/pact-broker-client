import requests
import json
from . import urls

from requests.auth import HTTPBasicAuth


def pull_contract(
    *,
    broker_url,
    provider,
    consumer,
    dir_path='.',
    version='latest',
    username=None,
    password=None,
):
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
    _save_contract(
        contract=response.json(),
        consumer=consumer,
        provider=provider,
        dir_path=dir_path
    )
    return response


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


def _save_contract(*, contract, consumer, provider, dir_path):
    consumer = consumer.replace(' ', '_')
    provider = provider.replace(' ', '_')
    file_path = f"{dir_path.rstrip('/')}/{provider}_{consumer}.json"
    with open(file_path, 'w') as contract_file:
        json.dump(contract, contract_file)
