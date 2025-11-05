class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @area.setter
    def area(self, new_area):
        if self.height == 0:
            raise ValueError("Balandlik 0 bo'lishi mumkin emas!")
        self.width = new_area / self.height


r = Rectangle(5, 10)
print(f"Birinchi maydon: {r.area}")
r.area = 100
print(f"Yangi kenglik: {r.width}")
print(f"Yangi maydon: {r.area}")
print("-" * 40)
