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
    def enum_windows_proc(hwnd, lParam):
        class_name = win32gui.GetClassName(hwnd)
        if class_name == 'ConsoleWindowClass':
            try:
                title = win32gui.GetWindowText(hwnd)
                print("[INFO] 当前遍历窗口名为：" + title)
                if title_name in title:
                    tid, pid = win32process.GetWindowThreadProcessId(hwnd)
                    print("[INFO] 已锁定程序为 PID: %d %d, title: %s" % (tid, pid, title))
                else:
                    pass
            except Exception, e:
                print("[WARN] error：", e)

    win32gui.EnumWindows(enum_windows_proc, None)





if __name__ == "__main__":
    pattern = 'hello'
    pids = find_cmd_processes(pattern)

