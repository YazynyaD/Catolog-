@echo off


:start
cls

set python_ver=36



cd \
cd C:\py\Scripts
pip install selenium
pip install eel openpyxl xlsxwriter
pip install xlsxwriter
pip install xlrd
pip install pandas
pip install openpyxl

pause
exit