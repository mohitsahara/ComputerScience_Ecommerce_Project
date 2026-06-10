@echo off
echo ====================================================
echo   TechMart E-Commerce Setup
echo ====================================================
echo.

echo [1/4] Installing dependencies...
pip3 install -r requirements.txt
echo.

echo [2/4] Running migrations...
py -3.10 manage.py makemigrations
py -3.10 manage.py migrate
echo.

echo [3/4] Populating sample data...
py -3.10 manage.py populate_data
echo.

echo [4/4] Starting development server...
echo.
echo  TechMart is running at: http://127.0.0.1:8000
echo  Admin panel:            http://127.0.0.1:8000/admin
echo  Admin credentials:      admin / admin123
echo  Coupon codes:           TECHMART10  WELCOME20  SAVE15
echo.
py -3.10 manage.py runserver
