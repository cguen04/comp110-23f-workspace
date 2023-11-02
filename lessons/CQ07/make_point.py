from lessons.CQ07.point import Point
my_point: Point = Point(20, 20)
my_point.scale_by(2)
second_point: Point = my_point.scale(3)
print(my_point)
print(second_point)

