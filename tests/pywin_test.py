import sys
from pywinauto import application

app = application.Application()

app.start_("C:\Users\John\Downloads\SharpTona.exe")


print(sys.version)
