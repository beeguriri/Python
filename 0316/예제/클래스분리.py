"""
class Game:
    def __init__(self, player_name, player_hp, player_attack, monster_name, monster_hp, monster_attack):
        self.player_name = player_name
        self.player_hp = player_hp
        self.player_attack = player_attack
        self.monster_name = monster_name
        self.monster_hp = monster_hp
        self.monster_attack = monster_attack

    def fight(self):
        while self.player_hp > 0 and self.monster_hp > 0:
            print(f"{self.player_name}의 체력: {self.player_hp}")
            print(f"{self.monster_name}의 체력: {self.monster_hp}")
            self.monster_hp -= self.player_attack
            print(f"{self.player_name}이 {self.monster_name}을 공격하여 {self.player_attack}의 데미지를 입혔습니다.")
            if self.monster_hp <= 0:
                print(f"{self.monster_name}을 물리쳤습니다.")
                break
            self.player_hp -= self.monster_attack
            print(f"{self.monster_name}이 {self.player_name}을 공격하여 {self.monster_attack}의 데미지를 입혔습니다.")
            if self.player_hp <= 0:
                print(f"{self.player_name}이 죽었습니다.")
                break

game = Game("Alice",120,15, "Goblin", 60, 8)
game.fight()
"""
class Player:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def attack_monster(self, monster):
        print(f"{self.name}이(가) {monster.name}을(를) 공격했습니다.")
        damage = self.attack
        monster.defend(damage)

    def defend(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name}이(가) 죽었습니다.")
        else:
            print(f"{self.name}의 체력이 {self.hp} 남았습니다.")

class Monster:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def attack_player(self, player):
        print(f"{self.name}이(가) {player.name}을(를) 공격했습니다.")
        damage = self.attack
        player.defend(damage)

    def defend(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            print(f"{self.name}이(가) 죽었습니다.")
        else:
            print(f"{self.name}의 체력이 {self.hp} 남았습니다.")

class Game:
    def __init__(self):
        self.player = None
        self.monster = None

    #클래스 내에서 다른 클래스의 객체 생성하여 사용
    def create_player(self, name, hp, attack):
        self.player = Player(name, hp, attack)

    #클래스 내에서 다른 클래스의 객체 생성하여 사용
    def create_monster(self, name, hp, attack):
        self.monster = Monster(name, hp, attack)

    def fight(self):
        while self.player.hp > 0 and self.monster.hp > 0:
            self.player.attack_monster(self.monster)
            if self.monster.hp <= 0:
                break
            self.monster.attack_player(self.player)
            if self.player.hp <= 0:
                break

game = Game()
game.create_player("Alice", 100, 10)
game.create_monster("Goblin", 50, 5)
game.fight()
