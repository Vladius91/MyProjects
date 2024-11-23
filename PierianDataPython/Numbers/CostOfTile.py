# Calculate the total cost of tile it would take to
# cover a floor plan of width and height, using a cost entered by the user.

pricePerTile = input("Enter an finctionary price for a single tile")
height = 10
width = 5

def AreaCalculator(w, h):
    return w * h

area = AreaCalculator(height,width)

def CostCalculator(area, price):
    return area * price

print(CostCalculator())
