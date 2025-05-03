from model.creature import Creature
import fake.creature as data


def get_all() -> list[Creature]:
    return data.get_all()


def get_one(name: str) -> Creature | None:
    return data.get(name)  # okay is the id and name mismatch on purpose?


def create(creature: Creature) -> Creature:
    return data.create(creature)


def replace(creature: Creature) -> Creature:
    return data.replace(id, creature)


def modify(name: str, creature: Creature) -> Creature:
    return data.modify(id, creature)


def delete(name: str) -> None:
    return data.delete(name)
