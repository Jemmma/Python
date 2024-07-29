# -*- coding: utf-8 -*-
# @Time     : 2024/7/23 13:57
# @Author  : Fizz
# @File     : win_cmd_kill.py
# @Description   : Hund sun

import win32gui
import win32process
import subprocess
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def find_cmd_processes(title_name):
    matching_pids = []
    print("[INFO] 你希望杀掉进程为：%s" % (title_name))
    def enum_windows_proc(hwnd, lParam):
        class_name = win32gui.GetClassName(hwnd)
        if class_name == 'ConsoleWindowClass':
            try:
                title = win32gui.GetWindowText(hwnd)
                print("[INFO] 当前遍历窗口名为：" + title)
                if title_name in title:
                    _, pid = win32process.GetWindowThreadProcessId(hwnd)
                    matching_pids.append(pid)
                    print("[INFO] 已锁定程序为 PID: %d, title: %s" % (pid, title))
                else:
                    pass
            except Exception, e:
                print("[WARN] error：", e)

    win32gui.EnumWindows(enum_windows_proc, None)

    return matching_pids


def stop_process_by_pids(pids):
    for pid in pids:
        try:
            print("[INFO] Ready to kill PID:", pids)
            subprocess.call(['taskkill', '/F', '/PID', str(pid)])
            print('Process with PID %d has been killed' % pid)
        except Exception, e:
            print('Error killing process with PID %d: %s' % (pid, e))


if __name__ == "__main__":
    pattern = sys.argv[1]
    pids = find_cmd_processes(pattern)
    stop_process_by_pids(pids)
