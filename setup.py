from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="bip39gen-nop",
    version="0.1.2",
    packages=find_packages(),

    package_data={
        '': ['*.txt']
    },

    author="Jay Carlson",
    author_email="nop@nop.com",
    description="Generate random BIP-039 wordlists",
    long_description=long_description,
    long_description_content_type='text/markdown',

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    license="MIT",
    keywords="bip39 bip039",
    url='https://github.com/nopdotcom/bip39gen',

    entry_points={
        'console_scripts': [
            'bip39gen = bip39gen.__main__:main'
        ]
    }
)
