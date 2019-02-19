# bip39gen: wordlist generator for Python

[Bitcoin BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) includes wordlists. These wordlists are useful for generating easily-typed but strongly random strings. The wordlists are 2048 words long, so each word carries 11 bits of information; a generated six-word passphrase has 66 bits of entropy, sufficient for most passwords.

This module does *not* attempt to encode or decode BIP39 keys; it just manages wordlists, and provides convenience methods for generating strongly random lists of words from them.

## `bip39gen` command

[`--lang` *lang*]

[`--separator` *separator*]

[`--count` *count*]

[*length*]

Generate *count* lines, each with *length* words, separated by *separator*.

Only the English (`en`) wordlist is shipped.
