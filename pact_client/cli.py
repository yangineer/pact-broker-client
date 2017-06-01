"""
Usage:
    pact_broker_client push --host host --file file --provider provider --consumer consumer [(--user user --password password)]
    pact_broker_client pull --host host --provider provider --consumer consumer [--dir dir] [(--user user --password password)]
    pact_broker_client (-h | --help)

Options:
    -h --help   Show this screen.
    --host  Pact Broker host.
    --file  Path to the pact file to be uploaded.
    --provider  Name fo the provider service.
    --consumer  Name fo the consumer service.
    --user  Username if authentication is required.
    --password  Password if authentication is required.
    push    Uploads a file to the pact broker.
    pull    Pulls a contract from the pact broker.
    --tag   Version or tag of the contract to upload/download.
    --dir   Directory to save the downloaded contract.

"""
import sys
import optparse

from commands import pull_contract


def exit_on_error():
    sys.stdout.write(__doc__)
    exit(2)


def handle_command(*, command, options=None):
    if command == 'pull':
        host = options.host
        consumer = options.consumer
        provider = options.provider
        dir_path = options.dir
        username = options.user
        password = options.password
        tag = options.tag

        if not any(host or consumer or provider):
            exit_on_error()

        result = pull_contract(
            broker_url=host,
            provider=provider,
            consumer=consumer,
            dir_path= dir_path or '.',
            version=tag or 'latest',
            username=username,
            password=password
        )

parser = optparse.OptionParser(usage=__doc__)

parser.add_option('--host')
parser.add_option('--file')
parser.add_option('--provider')
parser.add_option('--consumer')
parser.add_option('--user')
parser.add_option('--password')
parser.add_option('--dir')
parser.add_option('--tag')


options , args = parser.parse_args()

if not args:
    sys.stdout.write(__doc__)
    exit(2)

command = args[0]
handle_command(command=command, options=options)

