import datetime

class AnalyzeTriangle(object):
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    
    def validateTriangle(angle1, angle2, angle3):
        if angle1 + angle2 + angle3 != 180:
            print("Your angles do not add up to 180 degrees.")
        
        elif angle1 + angle2 + angle3 == 180:
            print("")

            if angle1 == angle2 == angle3:
                print("You have formed an: Equilateral Triangle")
        
            elif angle1 != angle2 != angle3:
                print("You have formed an: Scalene Triangle")
            
            elif angle1 == angle2 or angle1 == angle3 or angle2 == angle3:
                print("You have formed an: Isosceles Triangle")

angle1 = int(input("Please enter in the first angle: "))
angle2 = int(input("Please enter in the second angle: "))
angle3 = int(input("Please enter in the third angle: "))

triangle = AnalyzeTriangle.validateTriangle(angle1, angle2, angle3)

currentTime = datetime.datetime.now()

print("Todays date:", currentTime.strftime("%B %d %Y, todays time: %H:%M:%S"))