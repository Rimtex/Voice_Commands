import os
import ctypes
from apps.WindowMgr import WindowMgr
import psutil
import sys
import win32gui
import win32api
import win32con
import win32process

user32 = ctypes.WinDLL('user32', use_last_error=True)
user32.GetShellWindow.restype = ctypes.c_void_p


#: для получения названий окон
def get_window_process_path(hwnd):
    _, pid = win32process.GetWindowThreadProcessId(hwnd)
    hprocess = win32api.OpenProcess(win32con.PROCESS_QUERY_LIMITED_INFORMATION, False, pid)
    try:
        return win32process.GetModuleFileNameEx(hprocess, None)
    finally:
        hprocess.close()


def enum_func(hwnd, param):
    if param['hwnd'] is None:
        path = os.path.normcase(get_window_process_path(hwnd))
        if path == param['path']:
            text = win32gui.GetWindowText(hwnd)
            if os.path.normcase(os.path.basename(text)) == param['text']:
                param['hwnd'] = hwnd
    return True


shell_name = ''
shell_hwnd = user32.GetShellWindow()
if shell_hwnd:
    shell_path = get_window_process_path(shell_hwnd)
    shell_name = os.path.basename(shell_path)
if os.path.normcase(shell_name) != 'explorer.exe':
    sys.exit('The session shell must be Explorer.')

param = {
    'path': os.path.normcase(shell_path),
    'text': os.path.normcase(os.path.basename('C:\\Temp')),
    'hwnd': None,
}

print(get_window_titles())  # сама функция получения
my_list = get_window_titles()
windowCount = len([elem for elem in my_list if elem])
# indices = [i for i, x in enumerate(my_list) if x == "MPC-BE"]
mpc_srch = "MPC-BE"
matches = [match for match in my_list if mpc_srch in match]
mpc_fnd = matches


def check_if_exists(mpc, my_list):
    if mpc_srch in my_list:
        mpc_srch(str(mpc) + ' is inside the list')
    else:
        mpc_srch(str(mpc) + ' is not present in the list')


a = my_list
var = mpc_srch in (p.name() for p in psutil.process_iter())
if mpc_srch in a:
    print('MPC-BE is present!')
else:
    print('MPC-BE is not present')
print("Число не пустых открытых окон равно: " + f"{windowCount}" + f"  {var}" + f"  {matches}")

ihwnd = ""


def windowFocusPassingPID(pid):
    def callback(hwnd, list_to_append):
        list_to_append.append((hwnd, win32gui.GetWindowText(hwnd)))

    window_list = []
    win32gui.EnumWindows(callback, window_list)
    for pidOfProc in window_list:
        print(pidOfProc)  # if you want to check each item
        if pid == pidOfProc[0]:
            print(pidOfProc)  # printing the found item (id, window_title)
            win32gui.ShowWindow(pidOfProc[0], 5)
            win32gui.SetForegroundWindow(pidOfProc[0])
            pass


process_name = "Discord.exe"
for proc in psutil.process_iter():
    process = psutil.Process(proc.pid)  # Get the process info using PID
    pname = process.name()  # Here is the process name
    # print pname
    if pname == process_name:
        print(f"{process}" + " - Havewwwwwwwwwwwwwwwwww")
        windowFocusPassingPID(1816)
        # win32gui.ShowWindow(19964)
        # win32gui.EnumWindows(enum_func, param)
        win32gui.GetWindowText(param['hwnd'])

        w = WindowMgr()
        w.find_window_wildcard(".*Discord.*")
        w.set_active()  # - делаем активным\разворачиваем окно
        # w.set_background()   # - делаем неактивным\сворачиваем окно
        pass

    else:
        print(f"{process}" + " - Dont have")

#: