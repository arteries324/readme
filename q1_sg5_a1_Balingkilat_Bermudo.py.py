class hero:
    def __init__(you, name, hp):
        you.name=name
        you.hp=hp
    def take_damage(you, amount):
        you.hp -= amount
    def __str__(you):
        return f"{you.name}: {you.hp}hp"
arthur = hero("Arthur", 100)
morgana = hero("Morgana", 100)
arthur.take_damage(10)
print(arthur)
print(morgana)