import shutil

# Frames 0-100
for i in range(100):
	num = "{0:0>5}".format(i)
	pathName = '/Users/masonsayyadi/Desktop/frames/effect2_{}.png'.format(num)
	#print(pathName)
	shutil.copy2('/Users/masonsayyadi/Desktop/effect2_00000.png', pathName)


# Frames 250-350
for i in range(250,350):
	num = "{0:0>5}".format(i)
	pathName = '/Users/masonsayyadi/Desktop/frames/effect2_{}.png'.format(num)
	#print(pathName)
	shutil.copy2('/Users/masonsayyadi/Desktop/effect2_00250.png', pathName)


# Frames 750-850
for i in range(750,850):
	num = "{0:0>5}".format(i)
	pathName = '/Users/masonsayyadi/Desktop/frames/effect2_{}.png'.format(num)
	#print(pathName)
	shutil.copy2('/Users/masonsayyadi/Desktop/effect2_00750.png', pathName)


# Frames 1250-1350
for i in range(1250,1350):
	num = "{0:0>5}".format(i)
	pathName = '/Users/masonsayyadi/Desktop/frames/effect2_{}.png'.format(num)
	#print(pathName)
	shutil.copy2('/Users/masonsayyadi/Desktop/effect2_01250.png', pathName)