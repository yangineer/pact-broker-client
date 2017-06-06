import click

from .client import BrokerClient
from . import settings


@click.command()
@click.option('--broker_url', help='Pact Broker host.')
@click.option('--consumer', help='Consumer service name.')
@click.option('--provider', help='Provider service name.')
@click.option('--user', help='Pact Broker user.')
@click.option('--password', help='Pact Broker password.')
@click.option('--pact_dir', default='.', help='Directory to save path to.')
@click.option('--pact_version', default='latest', help='Pact version to pull.')
@click.option(
    '--auth',
    default=False,
    is_flag=True,
    help='Pact Broker is authenticated.'
)
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
        broker_url=broker_url or settings.PACT_BROKER_URL,
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
@click.option('--broker_url', help='Pact Broker host.')
@click.option('--consumer', help='Consumer service name.')
@click.option('--provider', help='Provider service name.')
@click.option('--user', help='Pact Broker user.')
@click.option('--password', help='Pact Broker password.')
@click.option('--pact_file', help='Path to the Pact to push.')
@click.option('--pact_version', help='Version of the new Pact.')
@click.option('--pact_dir', default='.', help='Directory to save path to.')
@click.option(
    '--auth',
    default=False,
    is_flag=True,
    help='Pact Broker is authenticated.'
)
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
        broker_url=broker_url or settings.PACT_BROKER_URL,
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
