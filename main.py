import math

def calculate_area_of_circle(radius):
    return math.pi * radius ** 2

def main():
    radius = float(input("Enter the radius of the circle: "))
    area = calculate_area_of_circle(radius)
    print(f"The area of the circle with radius {radius} is {area}")

if __name__ == "__main__":
    main()
