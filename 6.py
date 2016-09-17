import time
import platform
import os
import sys

def recorder():
    os.popen('top -bi | head -n 14 >> cpu_history.log')
    
    os.popen('cat cpu_history.log -n')


recorder()

