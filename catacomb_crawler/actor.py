import random

class Actor:
    def __init__(self, name: str, health: int, max_damage: int, x: int, y: int) -> None:
        self.name = name
        self.health = health
        self.max_damage = max_damage
        self.x = x
        self.y = y

    def is_alive(self) -> bool:
        return self.health > 0

    def has_escaped(self, size: int) -> bool:
        return self.x == size - 1 and self.y == size - 1

    def in_same_room(self, other: "Actor") -> bool:
        return self.x == other.x and self.y == other.y

    def in_adjacent_room(self, other: "Actor") -> bool:
        return (
            (self.x == other.x + 1 and self.y == other.y)
            or (self.x == other.x - 1 and self.y == other.y)
            or (self.x == other.x and self.y == other.y + 1)
            or (self.x == other.x and self.y == other.y - 1)
        )
        
    def deal_damage(self, other: "Actor") -> int:
        damage: int = random.randint(1, self.max_damage)
        other.health -= damage
        if not other.is_alive(): other.health = 0; 
        return damage
        
    def move(self, direction: str, size: int) -> bool:
        actor_was_moved: bool = True
        match (direction):
            case ("east"):
                if self.x == size - 1: 
                    actor_was_moved = False
                else:
                    self.x += 1
            case ("west"):
                if self.x == 0: 
                    actor_was_moved = False
                else:
                    self.x -= 1
            case ("south"):
                if self.y == size - 1: 
                    actor_was_moved = False
                else:
                    self.y += 1
            case ("north"):
                if self.y == 0: 
                    actor_was_moved = False
                else:
                    self.y -= 1
            case (_):
                actor_was_moved = False
        return actor_was_moved
                
    def __str__(self) -> str:
        return f"{self.name} at {self.x}, {self.y} with {self.health} health"
