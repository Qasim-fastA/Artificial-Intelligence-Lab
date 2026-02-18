class SimpleReflexAgent:
    def __init__(self, beds):
        self.beds = beds

    def check_beds(self):
        for i in range(len(self.beds)):
            if self.beds[i] == "Dry":
                print(f"Bed {i+1} is Dry , Watering...")
                self.beds[i] = "Moist"
            else:
                print(f"Bed {i+1} is Moist , Moving on...")

        print("\nFinal Bed Status:", self.beds)



beds = ["Moist", "Dry", "Moist", "Moist", "Dry", "Moist", "Dry", "Moist", "Moist"]
agent1 = SimpleReflexAgent(beds)
agent1.check_beds()
