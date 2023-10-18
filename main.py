class Building:
    def __init__(self, material, color, number=0):
        self.material = material
        self.color = color
        self._number = number  # Private attribute with underscore

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, new_number):
        if new_number >= 0:
            self._number = new_number
        else:
            print("Invalid number. Must be greater than or equal to 0.")

    @property
    def place(self):
        if self._number < 0:
            return "out of stock"
        elif 0 <= self._number < 100:
            return "warehouse"
        else:
            return "Remote warehouse"

# Create objects
brick = Building("white brick", "white", 300)
plank = Building("brown plank", "brown", 20)

# Print object variables using properties
print(f"Material: {brick.material}, Color: {brick.color}, Number: {brick.number}, Place: {brick.place}")
print(f"Material: {plank.material}, Color: {plank.color}, Number: {plank.number}, Place: {plank.place}")

# Add 50 bricks and remove 3 planks
brick.number += 50
plank.number -= 3

# Print object variables after modification
print(f"Material: {brick.material}, Color: {brick.color}, Number: {brick.number}, Place: {brick.place}")
print(f"Material: {plank.material}, Color: {plank.color}, Number: {plank.number}, Place: {plank.place}")
