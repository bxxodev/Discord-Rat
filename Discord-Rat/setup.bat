@echo off
python -m venv venv
call venv\Scripts\activate
pip install -r requirements.txt
echo All necessary packages have been installed.
pause
