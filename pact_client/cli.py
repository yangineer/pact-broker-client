import click


@click.command()
@click.option('--broker_url', help='Pact Broker host url.')
@click.option('--provider', help='Provider service name.')
@click.option('--consumer', help='Consumer service name.')
@click.option('--pact_dir', help='Directory to save the downloaded Pact.')
@click.option('--version', help='Version of the Pact to be downloaded.')
@click.option('--username', help='Pact Broker username.')
@click.option('--password', help='Pact Broker password.')
@click.option(
    '--auth',
    default=False,
    help='When True, username and password are required.'
)
def pull_pact(broker_url):
    """Command line tool to download Pact from a Pact Broker."""
    pass

if __name__ == '__main__':
    pull_pact()
