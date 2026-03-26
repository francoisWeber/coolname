import hashlib
import random
from typing import Any

from coolname.constants import ADJECTIVE, ADVERB, PLURALNOUN, VERB

_COMPONENTS = (
    ("adjective", ADJECTIVE),
    ("noun", PLURALNOUN),
    ("verb", VERB),
    ("adverb", ADVERB),
)


def _sha256(*args: Any) -> str:
    hasher = hashlib.sha256()
    for item in args:
        hasher.update(str(item).encode())
    return hasher.hexdigest()


def get_a_coolname(
    seed: Any = None,
    camel: bool = False,
    sep: str = "_",
    adjective: bool = True,
    noun: bool = True,
    verb: bool = True,
    adverb: bool = True,
) -> str:
    """Return a (predictable) random coolname that can act as a cool hash.

    The resulting coolnames have the shape: adjective + noun + verb + adverb.
    If seed is not None, it seeds a random generator so the output is
    deterministic (acts as a human-readable hash of the seed object).

    Example with a seed (acting like a hash):
    >>> get_a_coolname((42, "pythons", float))
    'apparent_lifeforms_freeze_randomly'

    Example without seed (random coolname):
    >>> get_a_coolname()
    'jovial_tigers_hug_silently'

    Parameters
    ----------
    seed : Any, optional
        Any Python object used as seed for a deterministic coolname.
    camel : bool, optional
        Use camelCase rather than snake_case, by default False.
    sep : str, optional
        Separator between words, by default "_".
    adjective : bool, optional
        Include an adjective, by default True.
    noun : bool, optional
        Include a noun, by default True.
    verb : bool, optional
        Include a verb, by default True.
    adverb : bool, optional
        Include an adverb, by default True.

    Returns
    -------
    str
        A coolname crafted based on the seed.
    """
    if seed is not None:
        seed = _sha256(seed)

    rng = random.Random(seed)
    flags = {"adjective": adjective, "noun": noun, "verb": verb, "adverb": adverb}
    phrase = [rng.choice(wordlist).lower() for name, wordlist in _COMPONENTS if flags[name]]

    if not phrase:
        phrase = ["nameless"]
    if camel:
        sep = ""
        phrase = phrase[:1] + [word.title() for word in phrase[1:]]

    return sep.join(phrase)
