
PUSH_PACT_URL = (
    '{broker_url}/pacts/provider/{provider}/consumer/'
    '{consumer}/version/{consumer_version}'
)
PULL_PACT_URL = (
    '{broker_url}/pacts/provider/{provider}/consumer/{consumer}/{pact_version}'
)

TAG_CONSUMER_URL = (
    '{broker_url}/pacticipants/{consumer}/versions'
    '/{consumer_version}/tags/{tag}'
)
