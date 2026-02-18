class GoalBasedAgent:
    def __init__(self, houses, goal):
        self.houses = houses
        self.goal = goal

    def search_goal(self):
        for house in self.houses:
            print(f"Visiting: {house}")
            if house == self.goal:
                print("Goal reached! Delivery done.")
                break



houses = ['Blue House', 'Green House', 'Red House', 'Yellow House', 'White House']
agent3 = GoalBasedAgent(houses, "Red House")
agent3.search_goal()
