class Polygon:
    def __init__(self, side, number_of_side, apothem):
        self.side = side
        self.number_of_side = number_of_side
        self.apothem = apothem

    def calculate_perimeter(self):
        return self.side*self.number_of_side

    def calculate_area(self):
        return ((self.calculate_perimeter() * self.apothem) / 2)

pentagon= Polygon(5,5,5)
print("The value of the area is:")
print(pentagon.calculate_area())
print("The value of the perimeter is:")
print(pentagon.calculate_perimeter())