@ECHO OFF
python M34OSExample2.py
IF %errorlevel%==-1 echo EXIT WITH ERROR
IF %errorlevel%==0 echo EXIT WITHOUT ERROR
