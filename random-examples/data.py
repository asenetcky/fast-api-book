from model import Creature

_creatures: list[Creature] = [
    Creature(
        name="yeti",
        country="CN",
        area="himalyas",
        description="Hirsute himalayan",
        aka="snowguy",
    ),
    Creature(
        name="squatch",
        country="US",
        area = "*",
        description="Yeti's cousin eddie",
        aka ="bigfoot",
    )
]

def get_creatures() -> list[Creature]:
    return _creatures