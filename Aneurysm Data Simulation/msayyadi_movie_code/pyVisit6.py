import sys
sys.path.append("/Applications/VisIt.app/Contents/Resources/3.1.1/darwin-x86_64/lib/site-packages/")
import visit


# Make a plot
#OpenDatabase("/Applications/VisIt.app/Contents/Resources/data/globe.silo")
OpenDatabase("/Users/masonsayyadi/aneurysm_tutorial_data/aneurysm_data/aneurysm*.silo database")

AddPlot("Pseudocolor", "pressure", 1, 1)
DrawPlots()

# Begin spontaneous state
View3DAtts = View3DAttributes()
View3DAtts.viewNormal = (-0.88317, 0.0685138, 0.464022)
View3DAtts.focus = (3.89585, 3.99132, 4.90529)
View3DAtts.viewUp = (0.0592263, 0.997645, -0.0345794)
View3DAtts.viewAngle = 30
View3DAtts.parallelScale = 2.05937
View3DAtts.nearPlane = -4.11875
View3DAtts.farPlane = 4.11875
View3DAtts.imagePan = (0, 0)
View3DAtts.imageZoom = 1.21
View3DAtts.perspective = 1
View3DAtts.eyeAngle = 2
View3DAtts.centerOfRotationSet = 0
View3DAtts.centerOfRotation = (3.89585, 3.99132, 4.90529)
View3DAtts.axis3DScaleFlag = 0
View3DAtts.axis3DScales = (1, 1, 1)
View3DAtts.shear = (0, 0, 1)
View3DAtts.windowValid = 1
SetView3D(View3DAtts)
# End spontaneous state

SetTimeSliderState(0)

sw = SaveWindowAttributes()
import math
for i in range(200):
	SetTimeSliderState(i)
	sw.family = 0
	sw.fileName = "frames/effect2_%05d" %(1350+i)
	SetSaveWindowAttributes(sw)
	SaveWindow()

import sys
sys.exit()