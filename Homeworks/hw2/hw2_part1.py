import math
length = raw_input("Length of rectangular prism (m) ==> " )
print length
width = raw_input("Width of rectangular prism (m) ==> ")
print width
height = raw_input("Height of rectangular prism (m) ==> ")
print height
def volume_prism(length, width, height):
    volume = length * width * height
    return volume
v = volume_prism(float(length), float(width), float(height))

total_water = float(6300.0 * float(v))

print "Water needed for","("+str(float(length))+"m,"+str(float(width))+"m,"+str(float(height))+"m) locks is "+str(total_water)+"m^3." 
radius = int(raw_input("Radius of cylinder (m) ==> "))
print radius
def find_length(radius, total_water):
    height_2 = total_water/(math.pi * radius**2)
    return height_2
h = find_length(float(radius), total_water)
print "Lake with radius",str(float(radius))+"m will lose %.1f"%(h)+"m depth in three months."

    