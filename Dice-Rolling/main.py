import random
class Dice:
    def __init__(self):
        self.max = 6
        self.min = 1
        self.DICE_ART = {
            1: (
                "┌─────────┐",
                "│         │",
                "│    ●    │",
                "│         │",
                "└─────────┘",
            ),
            2: (
                "┌─────────┐",
                "│  ●      │",
                "│         │",
                "│      ●  │",
                "└─────────┘",
            ),
            3: (
                "┌─────────┐",
                "│  ●      │",
                "│    ●    │",
                "│      ●  │",
                "└─────────┘",
            ),
            4: (
                "┌─────────┐",
                "│  ●   ●  │",
                "│         │",
                "│  ●   ●  │",
                "└─────────┘",
            ),
            5: (
                "┌─────────┐",
                "│  ●   ●  │",
                "│    ●    │",
                "│  ●   ●  │",
                "└─────────┘",
            ),
            6: (
                "┌─────────┐",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "│  ●   ●  │",
                "└─────────┘",
            ),
        }
        self.DIE_HEIGHT = len(self.DICE_ART[1])
        self.DIE_WIDTH = len(self.DICE_ART[1][0])
        self.DIE_FACE_SEPARATOR = " "
    def display_face(self, number):
        for i in range(self.DIE_HEIGHT):
            print(self.DICE_ART[number][i])

    def rolls(self):
        number = int(input("How many dices you want to roll?"))
        for i in range(0, number):
            random_number = random.randint(self.min, self.max)
            self.display_face(random_number)

d = Dice()
d.rolls()
