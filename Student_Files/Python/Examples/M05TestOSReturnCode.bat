@ECHO OFF
python M05OSReturnCode.py > out.txt
if %errorlevel%==-9 echo exited with error
if %errorlevel%==0 echo exited without error