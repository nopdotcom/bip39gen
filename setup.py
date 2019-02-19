from setuptools import setup, find_packages

setup(
    name="bip39gen",
    version="0.1.0",
    packages=find_packages(),

    package_data={
        '': ['*.txt']
    },

    author="Jay Carlson",
    author_email="nop@nop.com",
    description="Generate random BIP-039 wordlists",
    license="MIT",
    keywords="bip39 bip039",
    url='https://github.com/nopdotcom/bip39gen',

    entry_points={
        'console_scripts': [
            'bip39gen = bip39gen.__main__:main'
        ]
    }
)
