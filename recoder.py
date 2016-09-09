import os
import sys
import time

class Watcher():
    delay_time = 0
    filename = ""
    max_time = 0
    
    def __init__(self):
        self.delay_time = 60
        self.filename = "cpu.log"
        self.max_line = 840

    def set_time_delay(self, time_d):
        self.delay_time = time_d
    
    def set_filename(self, fn):
        self.filename = fn

    def set_max_line(self, max_d):
        self.max_line =  max_d

    def deal_with_log(self, rst):
        f = open(self.filename, 'w')
        for each in rst:
            print(each)
    
    def watch(self):
        pid = os.fork()
        if pid > 0:
            print('father,pid:' + str(pid))
            cmd = 'top -bi | head -n 14'
            rst = os.popen(cmd)
            print(rst)
            self.deal_with_log(rst)
        else:
            print("watcher running")


def deal_with_arg(watcher):
    for index, each in enumerate(sys.argv):
        print(each)
        if each == '-d':
            watcher.set_time_delay(sys.argv[index + 1])
        if each == '-f':
            watcher.set_filename(sys.argv[index + 1])
        if each == '-t':
            watcher.set_max_line(sys.argv[index + 1])

def main():
    watcher = Watcher()
    deal_with_arg(watcher)
    watcher.watch()
    
        
if __name__ == "__main__":
    main()

