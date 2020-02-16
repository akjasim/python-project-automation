@echo off
make_dir.py "%~1" "%~2"
if %ERRORLEVEL% NEQ 200 (
    EXIT /B 1
)
cd /d %~2\%~1
echo Creating virtual environment...
virtualenv venv
mkdir src
cd src
echo "%~1" > README.md
make_repo.py "%~1" "%~3"
if %ERRORLEVEL% NEQ 200 (
    EXIT /B 1
)
git init
git remote add origin https://github.com/%github_user%/%~1.git
git add .
git commit -m "first commit"
git push -u origin master
call ../venv/Scripts/activate
echo !!! Happy Coding !!!
echo Have a look at https://jasim.tech/
