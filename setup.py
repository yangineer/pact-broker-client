from setuptools import setup, find_packages

setup(
    name='pact-broker-client',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pull_pact=broker_client.cli:pull_pact
        push_pact=broker_client.cli:push_pact
    ''',
)
