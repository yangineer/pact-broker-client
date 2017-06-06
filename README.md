# pack_broker_client
Python client for the pact broker service


# Installation
To install, simply:
```
pip install pact-broker-client
```

# Command line usage
Use `pull_pact` to download a pact from the broker and `push_pact` upload a
pact to the broker.

To pull a pact simply run:
```
pull_pact --broker_url http://my.broker/ --provider "Provider Service"
--consumer "Consumer Service"
```

To push a pact to the broker run:
```
push_pact --broker_url http://my.broker/ --provider "Provider App"
--consumer "Consumer App" --pact_file pact.json --version 0.1.0
```

To see a full list of available option and what they do run `pull_pact --help`
or `push_pact --help`.

# Using as a module
When successful, The `pull_pact` and `push_pact` methods return a tuple with
a http response and a message.


```
from pact_broker.client import BrokerClient

broker_client = BrokerClient(broker_url='http://my.broker.url')

pull_pact_response, pull_pact_message = broker_client.pull_pact(
    provider=PROVIDER,
    consumer=CONSUMER
)

pull_pact_response, pull_pact_message = broker_client.push_pact(
    provider=PROVIDER,
    consumer=CONSUMER,
    pact_file=PACT_FILE_PATH,
    version=PACT_VERSION
)
```


# Contact
The project is maintained by Babylon Heath. You can get in touch at
`chatbot-developers@babylonhealth.com`.




