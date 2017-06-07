from setuptools import setup, find_packages

setup(
    name='pact-broker-client',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests>=2.17.3'
        'click>=6.7'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': [
            'pull_pact=pact_broker.cli:pull_pact',
            'push_pact=pact_broker.cli:push_pact'
        ]
    },
    license=read('LICENSE'),
    author='Babylon Health',
    author_email='chatbot-developers@babylonhealth.com'
)
