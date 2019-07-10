# pytesser
Python/.bat script for converting video credits into text files. Created way back while learning Python. 

Pytesser uses [ffmpeg](https://ffmpeg.org/download.html) and [tesseract](https://github.com/tesseract-ocr/tesseract/wiki) to perform all the heavy lifting. It also requires a pip install of the [Pytesseract](https://pypi.python.org/pypi/pytesseract/0.1) and [Pillow](https://python-pillow.org/) libraries. 

The script works by capturing images at each second for both the first and last two minutes of a video file. This number can be changed in outputCredits.bat's ffmpeg command if credits fall outside this range. Images are scanned with pytesser and results are sent to the Outputs folder. Logs listing the results of each image scan are also recorded. Pytesser supports .mov, .mp4, .mkv, and .avi out of box, but new formats can easily be added by editing outputCredits.bat. 

Simply drag the videos you want to scan into the accompanying folder and click outputCredits.bat. The script takes around 2 minutes per file and can handle multpile files at once. 
