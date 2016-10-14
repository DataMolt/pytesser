import pytesseract, os, glob, re, sys
from PIL import Image

images = glob.glob("ImageHolding/*.png")
images = [os.path.splitext(each)[0] for each in images]

if images == []:
    raw_input("No images found for scanning. You may have used an unspported video file. Check documentation for supported formats or edit outputCredits.bat to add your own. Press Enter to exit script.")
    sys.exit()

f = open("fs.txt", 'r')
files = f.read()
title = (re.findall(r':(.*?)\.',files)[0])

newFile = open("Outputs/%s_output.txt" % title, "w")
log = open("Logs/%s_log.txt" % title, "w")
log.write(title + "\n\n")

print "\n" + "Scanning " + title
credits = []
loglist =[]
for image in images:
    output = pytesseract.image_to_string(Image.open("%s.png" % image))
    if output == "":
        print ("%s has no data" % image)
        loglist.append("%s has no data" % image)
    elif output not in credits:
        print image
        loglist.append(image)
        credits.append(image)
        credits.append(output)

for row in credits:
    newFile.write(row + "\n\n\n")
newFile.close()

for row in loglist:
    log.write(row + "\n")
log.close()

images = glob.glob("ImageHolding/*.png")
for image in images:
    os.remove(image)

print "\n" + title + " completed. Results sent to Outputs folder."
