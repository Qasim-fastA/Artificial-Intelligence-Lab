class UtilityBasedAgent:
    def __init__(self, rocks):
        self.rocks = rocks

    def find_best_rock(self):
        best_utility = -999
        best_rock = None

        for rock, info in self.rocks.items():
            utility = (info["value"] * 2) - info["cost"]
            print(f"{rock} Utility = {utility}")

            if utility > best_utility:
                best_utility = utility
                best_rock = rock

        print(f"\nBest rock to sample: {best_rock}")


rocks = {
    "Rock A": {"value": 5, "cost": 2},
    "Rock B": {"value": 9, "cost": 8},
    "Rock C": {"value": 6, "cost": 3}
}
agent4 = UtilityBasedAgent(rocks)
agent4.find_best_rock()
