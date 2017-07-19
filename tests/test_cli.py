from mock import patch

from click.testing import CliRunner
from pact_broker import settings
from pact_broker.cli import pull_pact, push_pact


@patch('pact_broker.client.BrokerClient.pull_pact')
def test_cli_pull_pact(mock_pull_pact):
    broker_url = settings.PACT_BROKER_URL
    consumer = 'consumer'
    provider = 'provider'
    user = 'user'
    password = 'password'

    runner = CliRunner()
    result = runner.invoke(pull_pact, [
        '--broker_url', broker_url,
        '--consumer', consumer,
        '--provider', provider,
        '--auth',
        '--user', user,
        '--password', password,
        '--pact_dir', '.'
    ])
    assert result.exit_code == 0
    mock_pull_pact.assert_called_with(
        provider=provider,
        consumer=consumer,
        pact_version='latest'
    )


@patch('pact_broker.client.BrokerClient.push_pact')
def test_cli_push_pact(mock_push_pact):
    broker_url = settings.PACT_BROKER_URL
    consumer = 'consumer'
    provider = 'provider'
    user = 'user'
    password = 'password'
    pact_file = 'tests/stubs/test_pact.json'
    consumer_version = '0.1.0'

    runner = CliRunner()
    result = runner.invoke(push_pact, [
        '--broker_url', broker_url,
        '--consumer', consumer,
        '--provider', provider,
        '--auth',
        '--user', user,
        '--password', password,
        '--pact_file', pact_file,
        '--consumer_version', consumer_version
    ])
    assert result.exit_code == 0
    mock_push_pact.assert_called_with(
        provider=provider,
        consumer=consumer,
        consumer_version=consumer_version,
        pact_file=pact_file
    )


@patch('pact_broker.client.BrokerClient.tag_consumer')
@patch('pact_broker.client.BrokerClient.push_pact')
def test_push_pact_with_tag(mock_push_pact, mock_tag_consumer):
    broker_url = settings.PACT_BROKER_URL
    consumer = 'consumer'
    provider = 'provider'
    user = 'user'
    password = 'password'
    pact_file = 'tests/stubs/test_pact.json'
    consumer_version = '0.1.0'
    tag = 'dev'

    runner = CliRunner()
    result = runner.invoke(push_pact, [
        '--broker_url', broker_url,
        '--consumer', consumer,
        '--provider', provider,
        '--auth',
        '--user', user,
        '--password', password,
        '--pact_file', pact_file,
        '--consumer_version', consumer_version,
        '--tag', tag
    ])
    assert result.exit_code == 0, result.output
    mock_push_pact.assert_called_with(
        provider=provider,
        consumer=consumer,
        consumer_version=consumer_version,
        pact_file=pact_file
    )
    mock_tag_consumer.assert_called_with(
        provider=provider,
        consumer=consumer,
        consumer_version=consumer_version,
        tag=tag
    )
