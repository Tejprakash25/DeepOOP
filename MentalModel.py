class MentalModel:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I am {self.name}."

s1 = MentalModel("Alice")
s2 = MentalModel("Bob")

print(s1.introduce())  
print(s2.introduce())  
