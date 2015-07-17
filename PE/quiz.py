import math
side = 0
length = 0
'''x = input('0-3-  ')
for x in range(0, 4):
	a = (-5*x**5 +69*x**2-47)
	print (a)'''
'''def area_polygon(sides, length):
    area = (1/4)*(side*length**2)/math.tan(math.pi/side)
    return area'''
#import math
def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    print (point_x * scale, point_y * scale)
    
    #return print (point_x * scale, point_y * scale)
project_to_distance(2, 4, 2)
