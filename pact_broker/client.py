import requests
import json

from . import urls
from . import settings
from requests.auth import HTTPBasicAuth


class BrokerClient:

    def __init__(self, *, broker_url, pact_dir='.', user=None, password=None):
        self.broker_url = broker_url.rstrip('/') or settings.PACT_BROKER_URL
        self.username = user or settings.PACT_BROKER_USER
        self.password = password or settings.PACT_BROKER_PASSWORD
        self.pact_dir = pact_dir
        self.auth = None

        if settings.AUTHENTICATION_ON and not (
            self.username and self.password
        ):
            raise ValueError(
                'When authentication is True, username and password '
                'must be provided.'
            )
            self.auth = HTTPBasicAuth(self.username, self.password)

    def pull_contract(
        self,
        *,
        provider,
        consumer,
        pact_dir='.',
        version='latest',
    ):
        request_url = urls.PULL_CONTRACT_URL.format(
            broker_url=self.broker_url,
            provider=provider,
            consumer=consumer,
            version=version
        )

        response = requests.get(
            request_url,
            auth=self.auth
        )
        response.raise_for_status()
        saved_pact_path = self._save_contract(
            contract=response.json(),
            consumer=consumer,
            provider=provider
        )

        return response, f'Pact saved to {saved_pact_path}'

    def push_contract(self, *, pact_file, provider, consumer, version):
        request_url = urls.PUSH_CONTRACT_URL.format(
            broker_url=self.broker_url,
            provider=provider,
            consumer=consumer,
            version=version
        )

        with open(pact_file) as data_file:
            contract = json.load(data_file)

        response = requests.put(
            request_url,
            auth=self.auth,
            json=contract
        )
        response.raise_for_status()
        return response, (
            f'Pact with version:{version}'
            f'between {consumer} and {provider} pushed.'
        )

    def _save_contract(self, *, contract, consumer, provider):
        consumer = consumer.replace(' ', '_')
        provider = provider.replace(' ', '_')
        file_path = f'{self.pact_dir}/{provider}_{consumer}.json'.lower()

        with open(file_path, 'w') as contract_file:
            json.dump(contract, contract_file)

        return file_path
