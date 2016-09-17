#-*-coding:utf-8-*-
import os
import sys
import time
class watcher():
    total_count = 0
    delay = 0
    max_time = 0
    filename = ""

    def __init__(self):
        self.total_count = 0
        self.delay = 1
        self.max_time = 3
        self.filename = "cpu.log"

    def set_delay(self, time_d):
        self.delay = time_d
        print("set delay")

    def set_max_time(self, max_d):
        self.max_time = max_d

    def set_filename(self, fname):
        self.filename = fname

    def deal_with_log(self):
        fp = open(self.filename, 'a')
        now = time.asctime()
        fp.write('-------------------' + now + '--------------------\n')
        for each in os.popen('top -bn 1 | head -n 98'):
            fp.write(each)
        fp.write('\n')

    def watch(self):
        pid = os.fork()

        if pid > 0:

            while self.total_count < self.max_time:
                self.total_count += 1
                self.deal_with_log()
                time.sleep(self.delay)

            while self.total_count >= self.max_time:
                os.system('sed -i \'1, 100d\' cpu.log')
                self.deal_with_log()
                time.sleep(self.delay)

def deal_with_args(watcher):
    for index, arg in enumerate(sys.argv):
        if arg == 'd':
            watcher.set_delay(sys.argv[index + 1])
        if arg == '-f':
            watcher.set_filename(sys.argv[index + 1])
        if arg == '-t':
            watcher.set_max_time(sys.argv[index + 1])

def main():
    n_watch = watcher()
    deal_with_args(n_watch)
    n_watch.watch()

main()
