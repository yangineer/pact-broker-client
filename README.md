# pack_broker_client
Python client for the pact broker service


# Installation
To install, simply:
```
pip install pact-broker-client
```

# Usage
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

# Contact
The project is maintained by Babylon Heath. You can get in touch at
`chatbot-developers@babylonhealth.com`.




