pause

SET WRKDIR="%~dp0frontend"
SET PYTHON="C:\Users\Iurii_Pidvirnyi\AppData\Local\Programs\Python\Python36-32\python.exe"
#SET PYTHON="%~dp0Python36-32\python.exe"

SET SMOKE="%~dp0frontend\SmokeTestSuite.py"
SET SERVICE="%~dp0frontend\ServiceStatusTestCases.py"
SET LOGIN="%~dp0frontend\LoginTestCases.py"
SET DASHBOARD="%~dp0frontend\DashboardTestCasesMain.py"
SET NOTIFICATION="%~dp0frontend\DashboardTestCasesNotifications.py"
SET LIBRARY="%~dp0frontend\LibraryTestCases.py"
SET ENVUSER="%~dp0frontend\EnvironmentPreparationUser.py"
SET ENVDATA="%~dp0frontend\EnvironmentPreparationData.py"

ECHO OFF
CLS
:MENU
ECHO.
ECHO ...............................................
ECHO PRESS 1, 2, 3 ... OR 8 to select your task, or 9 to EXIT.
ECHO ...............................................
ECHO.
ECHO 1 - RUN Service Status Test Cases (headless mode)
ECHO 2 - RUN Login Test Cases (initial state)
ECHO 3 - RUN Dashboard Test Cases (initial state)
ECHO 4 - RUN Notification Test Cases (initial state)
ECHO 5 - RUN Library Test Cases (initial state)
ECHO 6 - RUN Environment Preparation User
ECHO 7 - RUN Environment Preparation Data
ECHO 8 - RUN Smoke Test Suite
ECHO 9 - EXIT
ECHO.

SET /P M=Type 1, 2, 3, 4, 5, 6, 7, 8 or 9 then press ENTER:
IF %M%==1 GOTO SERVICE
IF %M%==2 GOTO LOGIN
IF %M%==3 GOTO DASHBOARD
IF %M%==4 GOTO NOTIFICATION
IF %M%==5 GOTO LIBRARY
IF %M%==6 GOTO ENVUSER
IF %M%==7 GOTO ENVDATA
IF %M%==8 GOTO SMOKE
IF %M%==9 GOTO EOF

:SERVICE
%PYTHON% %SERVICE%
GOTO MENU
:LOGIN
%PYTHON% %LOGIN%
GOTO MENU
:DASHBOARD
%PYTHON% %DASHBOARD%
GOTO MENU
:NOTIFICATION
%PYTHON% %NOTIFICATION%
GOTO MENU
:LIBRARY
%PYTHON% %LIBRARY%
GOTO MENU
:ENVUSER
%PYTHON% %ENVUSER%
GOTO MENU
:ENVDATA
%PYTHON% %ENVDATA%
GOTO MENU
:SMOKE
%PYTHON% %SMOKE%
GOTO MENU
pause
%PYTHON% %SERVICE%
pause