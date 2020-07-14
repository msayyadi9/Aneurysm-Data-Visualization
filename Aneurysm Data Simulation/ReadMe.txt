Mason Sayyadi
University of Oregon

Link to YouTube movie: https://www.youtube.com/watch?v=LRrCC7LyOCw 

Description:

To make this movie I used a combination of VisIt, Python, Adobe Illustrator (Slides), and ffmpeg

Found an Aneurysm dataset and visualized it with VisIt. I used VisIt’s “command” function to autogenerate python code in which I iterated through in the form of multiple python files. Once the effects were done, I exported them to the frame folder, keeping in mind which numbers were generated for each effect. I then wrote another python file that copied and renamed a single image file (that contained my video titles) 100 times. I did this and specified the frame numbers I wanted them to be put at. 

I had the frame images and the python files I used all saved on my Desktop, with a directory called “frames” also on my desktop.

Command line commands to generate video: 

/Applications/VisIt.app/Contents/Resources/bin/visit -cli -s pyVisit.py
/Applications/VisIt.app/Contents/Resources/bin/visit -cli -s pyVisit2.py
/Applications/VisIt.app/Contents/Resources/bin/visit -cli -s pyVisit3.py
/Applications/VisIt.app/Contents/Resources/bin/visit -cli -s pyVisit4.py
/Applications/VisIt.app/Contents/Resources/bin/visit -cli -s pyVisit5.py
/Applications/VisIt.app/Contents/Resources/bin/visit -cli -s pyVisit6.py
/Applications/VisIt.app/Contents/Resources/bin/visit -cli -s pyVisit7.py
python3 cprname.py
ffmpeg -r 30 -f image2 -s 1920xq080 -I effect2_%05d.png -vcodec libx264 - crf 25 -pix_fmt yuv420p ../msayyadi_CIS410_project.mp4 