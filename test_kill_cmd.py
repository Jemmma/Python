# -*- coding: utf-8 -*-
# @Time     : 2024/7/23 17:54
# @Author  : Fizz
# @File     : test_kill_cmd.py
# @Description   : Hund sun
import subprocess

def stop_process_by_pids(pids):
    for pid in pids:
        try:
            print("[INFO] Ready to kill PID:", pids)
            subprocess.call(['taskkill', '/F', '/PID', str(pid)])
            print('Process with PID %d has been killed' % pid)
        except Exception, e:
            print('Error killing process with PID %d: %s' % (pid, e))


if __name__ == '__main__':
    pids = [15712]
    stop_process_by_pids(pids)