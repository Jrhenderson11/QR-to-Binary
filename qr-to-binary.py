import os
import numpy
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def qr_to_binary():
	print "enter file: (default qr.png)"
	fname = raw_input()
	if fname=="":
		fname = "qr.png"
	image1 = Image.open(fname, 'r')

	pixels = image1.load()
	width, height = image1.size

	file = open("qr.txt", 'w')
	for y in range(29):
		line = ""
		for x in range(29):

			#something
			colours = [0, 0]
			for y2 in range(height/29):
				for x2 in range(width/29):
					
					asd = ((x*height/29) + x2)
					asd2 = ((y*height/29) + y2)

					pixel =pixels[asd, asd2] 
					print pixel
					if (pixel == (0,0,0,255)):
						colours[1] = colours[1] + 1					
					else:
						colours[0] = colours[0] + 1
			m = 0
			
			#print colours[1]
			#print colours[0]

			if colours[1]>colours[0]:
				m=1
			line = line + str(m)

		file.write(line + "\n")
	file.close()
	print "saved to qr.txt"

qr_to_binary()
