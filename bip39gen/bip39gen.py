import secrets
from collections import OrderedDict
from typing import List, Tuple, Optional, Any, Mapping
import pkgutil

"""
Reading and generating random BIP-39 wordlists.
"""


def _lang_to_filename(lang: str = "en"):
    return "bip39-words.{0}.txt".format(lang)


class _Language(object):
    """Keep track of language-based bip39 wordlists/dictionaries"""

    def __init__(self, lang: str):
        words, reverse = _read_words(lang)
        self.words = words
        self.reverse = reverse

    instances: dict = {}

    @classmethod
    def get(cls, lang: str = "en") -> "_Language":
        existing = cls.instances.get(lang)
        if existing is not None:
            return existing
        lang_object = _Language(lang)
        cls.instances[lang] = lang_object
        return lang_object


def _wordlist_to_dict(t: Tuple) -> OrderedDict:
    d = OrderedDict((t[i], i) for i in range(len(t)))
    return d


def _read_words(lang: str = "en") -> Tuple[Tuple[str, ...], OrderedDict]:
    """This reads bip-words from the package this module is installed in."""
    path: str = _lang_to_filename(lang)
    data: Optional[bytes] = pkgutil.get_data(__package__, path)
    if data is None:
        raise FileNotFoundError("looking for language " + lang)
    data = data.strip()
    s = str(data, 'utf-8')
    t = tuple(s.split("\n"))
    return t, _wordlist_to_dict(t)


def words(lang="en") -> Tuple[str, ...]:
    """For a given language (default English), return an ordered tuple of bip39 words."""
    return _Language.get(lang).words


def reverse_dict(lang="en") -> OrderedDict:
    """For a given language (default English), return an ordered dict mapping bip39 words to their int equivalent."""
    return _Language.get(lang).reverse


def random_as_seq(n: int, lang="en") -> List[str]:
    """Return a strongly random list of n bip39 words in a given language (default English)"""
    l = _Language.get(lang)
    return [secrets.choice(l.words) for _ in range(n)]


def random_as_string(n: int, separator: str = " ", lang="en") -> str:
    """Return a single random string composed of n bip39 words in a given language, separated by spaces (by default)"""
    word_list: List[str] = random_as_seq(n, lang)
    return separator.join(word_list)
