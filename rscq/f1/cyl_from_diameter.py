import math

while True:
	diameter = float(input("diameter: "))
	length = float(input("length: "))

	vol_mm3 = (((int((diameter/2))^2)) * math.pi) * length

	print("VOLUME (MM CUBED): " + str(vol_mm3))
	print("VOLUME (CM CUBED): " + str(vol_mm3/1000))
