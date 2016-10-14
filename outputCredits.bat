dir /b *.mov>dir.txt
dir /b *.mp4>>dir.txt
dir /b *.mkv>>dir.txt
dir /b *.avi>>dir.txt
findstr /n . dir.txt>fsn.txt
find /c "." dir.txt>find.txt
for /f "tokens=3" %%x in (find.txt) do set total=%%x
set count=0


:count
set /a count=%count%+1
findstr /b %count%: fsn.txt>fs.txt
for /f "tokens=2 delims=:" %%x in (fs.txt) do set "filename=%%~nx"
for /f "tokens=2 delims=:" %%x in (fs.txt) do set "fileext=%%~xx"


ffmpeg -i %filename%%fileext% -t 00:02:00 -vf fps=1 ImageHolding/aOut%%04d.png
ffmpeg -sseof -00:02:00 -i %filename%%fileext% -vf fps=1 ImageHolding/bOut%%04d.png
pytess.py


if not %count% geq %total% goto count
echo Scanning completed. %total% files scanned.
del *.txt
pause
