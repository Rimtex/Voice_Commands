import os
import pygetwindow
import win32com
import win32com.client as wincl


# создание ярлыка + запуск с него
def create_shortcut(shortcut_name, target_script_path):
    path_to_shortcut = ""  # папка ярлыков
    try:
        shortcut_if_create = pygetwindow.getWindowsWithTitle(shortcut_name)[0]
        shortcut_if_create.moveTo(88, 220)
        shortcut_if_create.resizeTo(849, 327)
    except Exception as e:
        print(f"\r                                               (!o_O) ярлык --> {shortcut_name}\r")
        script_path = target_script_path
        script_directory = os.path.dirname(script_path)
        shortcut_name_link_path = os.path.join(script_directory, path_to_shortcut + shortcut_name + ".lnk")
        if not os.path.isfile(shortcut_name_link_path):
            shell = win32com.client.Dispatch("WScript.Shell")
            shortcut = shell.CreateShortCut(shortcut_name_link_path)
            shortcut.TargetPath = "python.exe"
            shortcut.Arguments = script_path
            shortcut.Description = shortcut_name
            shortcut.WorkingDirectory = script_directory
            shortcut.Save()
        print(e)
        os.startfile(path_to_shortcut + shortcut_name)
        exit()

# пример использования
# create_shortcut("ассистент", os.path.abspath(__file__))
