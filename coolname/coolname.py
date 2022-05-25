import random
import hashlib
from typing import Any
from coolname.constants import ADJECTIVE, PLURALNOUN, VERB, ADVERB


def sha256(*args):
    sha1_creator = hashlib.sha256()
    for item in args:
        sha1_creator.update(str(item).encode())
    return sha1_creator.digest().hex()


def get_a_coolname(
    seed: Any = None,
    camel: bool = False,
    sep: str = "_",
    adjective: bool = True,
    noun: bool = True,
    verb: bool = True,
    adverb: bool = True,
) -> str:
    """get_a_coolname returns a (predictible) random coolname that can act as a (cool) hash
    The resulting coolnames have the following shape : adjective + noun + verb + adverb.
    If seed is not None, then this object will seed a random generator. In this case, the
    output of the function will act as a (cool) hash of the seed-object

    Example with a seed (acting like a hash):
    > get_a_coolname((42, "pythons", float))
    >> 'apparent_lifeforms_freeze_randomly'
    > get_a_coolname((42, "pythons", float))
    >> 'apparent_lifeforms_freeze_randomly'
    > get_a_coolname((42, "pythons", float))
    >> 'apparent_lifeforms_freeze_randomly'

    Example wthout seed (random coolname):
    > get_a_coolname()
    >> 'jovial_tigers_hug_silently'
    > get_a_coolname()
    >> 'furious_eagles_argue_highly'

    Parameters
    ----------
    seed : Any, optional
        Any Python object to be used as seed to get a hash-like coolname, by default None
    camel : bool, optional
        Use camel-case rather than snake-case, by default False
    sep : str, optional
        separator for your cool-name's members, by default "_"
    adjective : bool, optional
        Should the coolname contain an adjective, by default True
    noun : bool, optional
        Should the coolname contain a noun, by default True
    verb : bool, optional
        Should the coolname contain a verb, by default True
    adverb : bool, optional
        Should the coolname contain an adverb, by default True

    Returns
    -------
    str
        A coolname crafted based on the seed
    """
    # Use custom SHA256 to be able to seed from anything
    if seed is not None:
        seed = sha256(seed)

    # Now get the different component from this seeded RNG
    phrase = []
    if adjective:
        phrase += random.Random(seed).choice(ADJECTIVE).lower()
    if noun:
        phrase += random.Random(seed).choice(PLURALNOUN).lower()
    if verb:
        phrase += random.Random(seed).choice(VERB).lower()
    if adverb:
        phrase += random.Random(seed).choice(ADVERB).lower()

    if len(phrase) == 0:
        phrase = ["nameless"]
    if camel:
        sep = ""
        phrase = phrase[:1] + [word.title() for word in phrase[1:]]

    return sep.join(phrase)
