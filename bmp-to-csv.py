import os
import numpy
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def print_intro():
	print "       _______"
	print "      /    \\\\\\\\"
	print "     /  /\  \\\\\\\\"
	print "    /  ///\  \\\\\\\\"
	print "   /  //// \__\\\\\\\\"
	print "   \  \\\\\\\\ /  ////"
	print "    \  \\\\\\\\  ////"
	print "     \  \\\\\\\\////"
	print "      \  \\\\\///"
	print "       `''''''"

def bmp_to_csv():
	print "enter file: (default map.bmp)"
	fname = raw_input()
	if fname=="":
		fname = "map.bmp"
	image1 = Image.open(fname, 'r')

	pixels = image1.load()
	width, height = image1.size
	#load pixel data into array
	#print "enter width to save as"
	#w = raw_input()
	#print "enter height to save as"
	#h = raw_input()

	file = open("map.txt", 'w')
	for y in range(height):
		line = ""
		for x in range(width):
			val = 1

			if (pixels[x, y] == (255,255,255)):
				val=0
			if (not x==width-1):
				line = line + str(val) +","
			else:
				line = line + str(val)

		file.write(line + "\n")
	file.close()
	print "saved to map.txt"
print_intro()
bmp_to_csv()
