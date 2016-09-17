import os
import sys
import time

class watcher(self,delay_time, file_name, max_time):
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
        self.max_line = 

    def deal_with_log(self, log):
        for index, line in enumrate(log.readline()):
            if log[index] > 10
    
    def watch(self):
        pid = os.fork()
        if pid > 0:
            print('father,pid:' + pid)
            log = os.popen('top -bi | head -n 14 >> cpu_history.log')
            self.deal_with_log(log)
        else:
            print("watcher running")


def deal_with_arg(tmp):
    for index, each in enumrate(sys.argv):
        print(each)
        if each == '-d':
            watcher.set_time_delay(sys.argv[index + 1])
        if each == '-f':
            watcher.set_filename(sys.argv[index + 1])
        if each == '-t':
            watcher.set_max_time(sys.argv[index + 1])
        
if __name__ == "__main__":
    tm = 3
    run_recorder(tm)

