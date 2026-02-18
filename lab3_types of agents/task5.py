import random

class LearningAgent:
    def __init__(self):
        self.spots = ["Start", "Empty", "Cheese", "Trap"]
        self.rewards = {
            "Start": 0,
            "Empty": -1,
            "Cheese": 10,
            "Trap": -10
        }
        self.position = "Start"

    def move_randomly(self):
        print("Mouse starts at Start.")
        new_spot = random.choice(self.spots[1:])
        print(f"Mouse moved to: {new_spot}")
        print("Reward:", self.rewards[new_spot])



agent5 = LearningAgent()
agent5.move_randomly()
