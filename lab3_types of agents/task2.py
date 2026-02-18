class ModelBasedAgent:
    def __init__(self):
        self.has_key = False
        self.path = ["A", "C", "D", "B", "D"]

    def patrol(self):
        for room in self.path:
            print(f"\nRobot entering Room {room}")

            if room == "D":
                if self.has_key:
                    print("access granted to high-security vault.")
                else:
                    print("access denied Keycard required.")

            if room == "B":
                print("Keycard found! Picking it up.")
                self.has_key = True



agent2 = ModelBasedAgent()
agent2.patrol()
