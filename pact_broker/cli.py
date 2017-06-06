import click

from .client import BrokerClient
from . import settings


@click.command()
@click.option('--broker_url')
@click.option('--consumer')
@click.option('--provider')
@click.option('--user')
@click.option('--password')
@click.option('--auth', default=False, is_flag=True)
@click.option('--pact_dir', default='.')
@click.option('--pact_version', default='latest')
def pull_pact(
    broker_url,
    consumer,
    provider,
    user,
    password,
    auth,
    pact_dir,
    pact_version
):
    settings.AUTHENTICATION_ON = auth

    broker_client = BrokerClient(
        broker_url = broker_url or settings.PACT_BROKER_URL,
        pact_dir=pact_dir or settings.PACT_DIR,
        user=user or settings.PACT_BROKER_USER,
        password=password or settings.PACT_BROKER_PASSWORD
    )

    result = broker_client.pull_pact(
        consumer=consumer,
        provider=provider,
        version=pact_version
    )

    click.echo(result[1])


@click.command()
@click.option('--broker_url')
@click.option('--consumer')
@click.option('--provider')
@click.option('--user')
@click.option('--password')
@click.option('--auth', default=False, is_flag=True)
@click.option('--pact_file')
@click.option('--pact_version')
@click.option('--pact_dir', default='.')
def push_pact(
    broker_url,
    consumer,
    provider,
    user,
    password,
    auth,
    pact_file,
    pact_version,
    pact_dir
):
    settings.AUTHENTICATION_ON = auth

    broker_client = BrokerClient(
        broker_url = broker_url or settings.PACT_BROKER_URL,
        pact_dir=pact_dir or settings.PACT_DIR,
        user=user or settings.PACT_BROKER_USER,
        password=password or settings.PACT_BROKER_PASSWORD
    )

    result = broker_client.push_pact(
        consumer=consumer,
        provider=provider,
        pact_file=pact_file,
        version=pact_version
    )

    click.echo(result[1])