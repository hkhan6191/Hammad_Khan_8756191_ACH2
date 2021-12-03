class Rectangle(object):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        return(length, width)

    def getArea(length, width):
        area = length*width
        return area

    def getPerimeter(length, width):
        perimeter = 2*(length+width)
        return perimeter

    def showResults(length, width):
        print("Area =", int(area))
        print("Perimeter =", int(perimeter))

length = int(input("Please enter in the length of your rectangle (ft):"))
width = int(input("Please enter in the width of your rectangle (ft):"))

area = Rectangle.getArea(length, width)
perimeter = Rectangle.getPerimeter(length, width)
results = Rectangle.showResults(length, width) 