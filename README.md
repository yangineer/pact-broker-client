# pack_broker_client
Client for the pact broker service


# Install
```
pip install pact-broker-client
```

# From source
```
python setup.py develop
```

# Usage
Use `pull_pact` to download a pact from the broker and `push_pact` upload a
pact to the broker.

The option `pull_pact --help` or `push_pact --help` will display the help page
for that command.

Usage: pull_pact [OPTIONS]

  Command line tool to pull pacts from a Pact Broker.

Options:
  --broker_url TEXT  Pact Broker host url.
  --provider TEXT    Provider service name.
  --consumer TEXT    Consumer service name.
  --pact_dir TEXT    Directory to save the downloaded Pact.
  --version TEXT     Version of the Pact to be downloaded.
  --username TEXT    Pact Broker username.
  --password TEXT    Pact Broker password.
  --auth TEXT        When True, username and password are required.
  --help             Show this message and exit.

Usage: push_pact [OPTIONS]

  Command line tool to push pacts from a Pact Broker.

Options:
  --broker_url TEXT  Pact Broker host url.
  --provider TEXT    Provider service name.
  --consumer TEXT    Consumer service name.
  --pact_file TEXT   Pact file to be push to the broker.
  --version TEXT     Version of the Pact.
  --username TEXT    Pact Broker username.
  --password TEXT    Pact Broker password.
  --auth TEXT        When True, username and password are required.
  --help             Show this message and exit.



