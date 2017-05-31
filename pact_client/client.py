import requests
import json

from requests.auth import HTTPBasicAuth
from . import urls


def get_contract(
    *,
    broker_url,
    provider,
    consumer,
    version='latest',
    username=None,
    password=None,
):
    request_url = urls.GET_CONTRACT_URL.format(
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
    return response


def put_contract(
    *,
    contract_path,
    broker_url,
    provider,
    consumer,
    version='latest',
    username=None,
    password=None,
):
    request_url = urls.GET_CONTRACT_URL.format(
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
