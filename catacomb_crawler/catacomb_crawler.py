import random
import sys

from actor import Actor


def make_hero() -> Actor:
    print("What is your name, heroic adventurer?")
    hero_name: str = input("> ")

    return Actor(name=hero_name, health=100, max_damage=10, x=0, y=0)


def get_dungeon_size() -> int:
    while True:
        print("How wide of a catacomb do you want to face (5-10)?: ")
        size: int = int(input("> "))

        if size >= 5 and size <= 10:
            break
        else:
            print("That is not a valid catacomb size!")
    return size


def is_monster_at_coords(x: int, y: int, monsters: list[Actor]) -> bool:
    if len(monsters) == 0:
        return False

    for monster in monsters:
        if monster.x == x and monster.y == y:
            return True
    return False


def make_monsters(size: int) -> list[Actor]:
    num_monsters: int = int((size * size) / 6)
    monsters: list[Actor] = []

    x: int = random.randint(0, size - 1)
    y: int = random.randint(0, size - 1)

    for i in range(0, num_monsters):
        while (
            is_monster_at_coords(x, y, monsters)
            or (x == 0 and y == 0)
            or (x == size - 1 and y == size - 1)
        ):
            x = random.randint(0, size - 1)
            y = random.randint(0, size - 1)

        new_monster: Actor = Actor(
            name=f"Monster {i}", health=25, max_damage=5, x=x, y=y
        )
        monsters.append(new_monster)
    return monsters


def fight(hero: Actor, monsters: list[Actor]) -> None:
    for monster in monsters:
        if hero.in_same_room(monster):
            print(f"{hero} versus {monster}")
            while hero.is_alive() and monster.is_alive():
                print(f"You hit for {hero.deal_damage(monster)} damage")
                print(f"You get hit for {monster.deal_damage(hero)} damage")

            if not hero.is_alive():
                sys.exit("You died in combat! Game over!")
            else:
                print(f"{monster.name} has been defeated!")
                monsters.remove(monster)


def count_nearby_monsters(hero: Actor, monsters: list[Actor]) -> int:
    count: int = 0
    for monster in monsters:
        if hero.in_adjacent_room(monster):
            count += 1
    return count


def print_hero_and_smell_count(hero: Actor, monsters: list[Actor]) -> None:
    print(hero)
    num_nearby_monsters: int = count_nearby_monsters(hero, monsters)
    print(f"You smell {num_nearby_monsters} monsters nearby.")


def move(hero: Actor, monsters: list[Actor], size: int) -> None:
    print("Which way do you want to go (north, south, east, west)? ")
    user_input: str = input("> ").lower()

    if not hero.move(user_input, size):
        print("You can't move that way!")
    else:
        if hero.has_escaped(size):
            sys.exit("You have escaped the catacomb!")

        hero.health -= 2
        if not hero.is_alive():
            sys.exit("You died in the catacomb! Game over!")

        fight(hero, monsters)
        print_hero_and_smell_count(hero, monsters)


def main() -> None:
    hero: Actor = make_hero()
    size: int = get_dungeon_size()
    monsters: list[Actor] = make_monsters(size)

    print_hero_and_smell_count(hero, monsters)
    while True:
        move(hero, monsters, size)


if __name__ == "__main__":
    main()
